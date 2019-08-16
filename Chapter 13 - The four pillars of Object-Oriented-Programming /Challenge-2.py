#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Fri Aug 16 19:20:06 2019

Challenge 2 , create a method in Square called change size that lets you increase
or decreas the side of the triangle.

@author: zordo

"""
import sys 
    



class Square():
    
    
    def __init__(self, l):
        self.lenght = l 
        print(self.lenght)
    
    def calculate_perimeter(self):
         return (self.lenght * 4 )
    
    
    def change_size(self,n):
        
        self.lenght = self.lenght + n
        if self.lenght < 0 :
            
       
            sys.exit("You can't decrease more bro !")
            
        




sqr =  Square(2)

print(sqr.calculate_perimeter())     

sqr.change_size(-3)

print(sqr.calculate_perimeter())