#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 22:19:12 2019

@author: zordo
"""

# Write aporgame with two functions. The first should take an integer as a 
#parameter ans return the result of the integer divided by 2.
#The second should take an integer as a parameter and return the result of 
# the integer multiplied by 4 
# Call the first function, save the result of as a variable and pass it as 
# parameter to the second function


def function_one(x) :
    """
    returns integer input divided by 2 
    
    :params x: int.
    :return: int x divided by 2 
    
    """
    
    return x/2 


def function_two(x) :
    """
    returns integer multiplied by 4 
    
    :param x: integer 
    :return: int x multiplied by 4 
    
    """
    
    return x*4



y = function_one(2)


function_two(y)