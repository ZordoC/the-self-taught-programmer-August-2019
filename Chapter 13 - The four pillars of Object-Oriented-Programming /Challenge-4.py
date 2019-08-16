#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 19:39:48 2019

Challenge-4 Create a class called Horse and a class called Rider , use 
composition to model a horse that has a rider 

@author: zordo
"""



class Horse():
    
    def __init__(self,w,h,c,o):
        self.weight = w
        self.height = h
        self.colour = c 
        self.owner = o
        
        
    

class Rider():
    
    def __init__(self,name):
        self.name = name




jose = Rider("Jose Conceicao")

horsie = Horse(300,160,'gray',jose)

print(horsie.owner.name)    