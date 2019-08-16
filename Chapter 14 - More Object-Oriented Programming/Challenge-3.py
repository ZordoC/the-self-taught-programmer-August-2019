#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 20:10:16 2019

Challenge 3 - Write a function that takes two objects as parameters and returns 
True if they are the saem object, and False if they are not 

@author: zordo
"""



def same_obj(obj1,obj2):
    
    print(obj1 is obj2)



class chair():
    
    def __init__(self,c):
        self.colour = c 
        

chair1 = chair('brown')

chair_same_as_1 = chair1

chair2= chair('brown')


same_obj(chair1,chair2)        

print("\n")

same_obj(chair1,chair_same_as_1)