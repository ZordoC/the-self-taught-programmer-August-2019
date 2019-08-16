#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 22:23:38 2019

@author: zordo
"""

# Write a function that converts a string to float and returns the result ,
# use expection handling to catch exceptions that might occur. 


def convert_str_to_float(string):
    """
    converts string to float, handling exception ValueError 
    
    
    :param string: string.
    :return: string converted to float .
    
    
    """
    try:
        
       return float(string)
    
    except ValueError : 
        
        print('It has to be a numerical value !! ')
    
    
    
print(convert_str_to_float('3.6'))
    
print(convert_str_to_float('hola'))    

