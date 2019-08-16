#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 18:40:06 2019

Create a tringale class with a method called area that calculates 
and returns its area, call area on it and print the result 


@author: zordo
"""



class Triangle():
    
    def __init__(self,b,h):
        self.base = b
        self.height = h
        print("Created a triangle for you sir ! ")
    
    
    
    def area(self):
        
        return (self.base * self.height) / 2  
    
    


tri = Triangle(2,4)

tri_area = tri.area()

print(tri)    
print("\n")
print(tri_area)


        
        



            
