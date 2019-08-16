#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 19:10:18 2019

Challenge -1  Create Square and REctangle classes witha mehtod called 
calculate_perimeter tahta calculate the pererimeter of the shapes they represent
create the objects and call the method on both of them


@author: zordo
"""



class Square():
    
    def __init__(self, l):
        self.lenght = l 
        
        
    def calculate_perimeter(self):
        
        return (self.lenght * 4 )
    


class Rectangle():    
        
   def __init__(self,l,h):
        self.lenght = l 
        self.height = h
        
   def calculate_perimeter(self):
        
        return (self.lenght * 2 + self.height * 2 )
    
    


rect =  Rectangle(2,4)

print(rect.calculate_perimeter())

square = Square(2)

print(square.calculate_perimeter()) 
    
    



    
         
        