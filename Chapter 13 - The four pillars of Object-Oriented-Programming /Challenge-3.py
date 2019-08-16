#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 19:31:21 2019

Challenge 3 - Create a class called Shape. Define a method init called
what_am_i  that prints "I am a shape " when called , 
Change your Square and Recatangñle classes from the previous challenges to 
inherit shape , create Square and REctangel object and call the new method on 
both of them

@author: zordo
"""

class Shape():
    
    def what_am_I(self):
        print("I am a Shape")        
                    
    


class Square(Shape):
    
    def __init__(self, l):
        self.lenght = l 
        
        
    def calculate_perimeter(self):
        
        return (self.lenght * 4 )

class Rectangle(Shape):    
        
   def __init__(self,l,h):
        self.lenght = l 
        self.height = h
        
   def calculate_perimeter(self):
        
        return (self.lenght * 2 + self.height * 2 )
    
    
sqr = Square(2)

rect = Rectangle(2,3)

sqr.what_am_I()

rect.what_am_I()
    