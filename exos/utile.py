#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 18:43:29 2018

@author: lepetit
"""



# Replace the dictionary by the content of the key "region_attributes"
def simplify_annotations(data):
    for key, value in data.items():
        if 'filename' in value:
            del value['filename']
        if 'file_attributes' in value:
            del value['file_attributes']
        classe_echo_set = set()
        for region in value['regions']:
          # print(region['region_attributes'])
          if 'classe-echo' in region['region_attributes']:
            classe_echo_set.update(region['region_attributes']['classe-echo'].keys())
        value['regions'] = '_'.join(classe_echo_set)
    return data

