#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 18:26:05 2019

Challenge -1 Create a class caleed apple with 4 attributes

@author: zordo
"""



class Apple():
    def __init__(self,w,c,s,r):
        self.weight = w 
        self.colour = c 
        self.species = s 
        self.radius = r
        print("Object created")
        


apple = Apple(100,'red','Pink Lady',10)   




print(apple)     

print("\n")

print(apple.weight)       

print("\n")

print(apple.colour)       

print("\n")

print(apple.species)        

print("\n")

print(apple.radius)    

print("\n")
    

