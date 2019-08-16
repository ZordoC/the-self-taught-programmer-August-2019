#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 18:34:17 2019

Create a circle class with a method area that calculaed and retuns its area,
then create a Circle object, call area on it and print the reslut. Use python's
pi function from the math module  


@author: zordo
"""



import math 



class Circle():
    def __init__(self,r):
        self.radius = r 
        print("Created Circle")
        
        
        
        
    def area(self):
        return self.radius * self.radius * math.pi 
    
    
    
    
my_circle =  Circle(10)

my_circle_area = my_circle.area()     

print(my_circle)

print("\n")

print(my_circle_area)   