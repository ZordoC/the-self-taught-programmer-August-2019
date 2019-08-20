#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 01:01:50 2019

Count Characthers Occurences 

@author: zordo
"""


def count_characters(string):
    count_dict = {}
    for c in string:
        
        if c in count_dict:
            count_dict[c] += 1
            
        else:
            count_dict[c] = 1
            
    print(count_dict)
        
        

count_characters("Wallet")
