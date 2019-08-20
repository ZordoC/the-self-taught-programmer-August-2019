#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 00:52:26 2019

Sequential Search 

@author: zordo
"""

def ss(number_list,n):
    found = False
    
    for i in number_list:
        if i ==n:
            found = True
            break
    return found


numbers =  range(0,100)

s1 = ss(numbers,2)

print(s1)



