#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 22:16:45 2019

@author: zordo
"""

# Challenge 3 wirte a function that takes three required parameters and two 
# optional parameters

def parameters_function(x,y,z,w=4,k=5):
    """
    
    prints all parameters of the function
    
    :param x: int, float , str 
    :param y: int, float, str
    :param z: int, float, str
    :param w: optional param initialized with 4 
    :param k: optional param initialized with 5 
    
    """
    
    print(x)
    print(y)
    print(z)
    print(w)
    print(k)
    
    return 



parameters_function(1,2,3)

print("\n")

parameters_function(4,4,3)