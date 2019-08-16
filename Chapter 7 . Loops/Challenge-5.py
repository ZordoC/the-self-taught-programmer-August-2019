#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 01:15:08 2019

@author: zordo
"""

#Challenge 5 - Multiply all numbers in the list [8, 19 ,148 ,4 ] with all 
# the numbers in the list [9,1,33,83], and append each result to a third list 


list1 = [8,19,148,4]

list2 = [9,1,33,83]

list3 = []

for i,nums in enumerate(list1):
    for j, numss in enumerate(list2):
        list3.append(list1[i]*list2[j])
        

print(list3)        




        
        
    