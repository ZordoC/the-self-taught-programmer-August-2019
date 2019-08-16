#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 18:44:28 2019

Challenge 4 make an Hexagon class with a method called calculate peremiter that
calculates and returns it's perimeter, then create the object call the method 
and print the result 

@author: zordo
"""


class Hexagon():
    
    def __init__(self,l):
        self.l = l
        print("Created Hexagon")
        
        
        
    def calculate_perimeter(self):
        
        return (self.l * 6 )
    
    
        


hexa = Hexagon(2)

hexa_perimeter = hexa.calculate_perimeter()

print(hexa)

print("\n")

print(hexa_perimeter)        
    
