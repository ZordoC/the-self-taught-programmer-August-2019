#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 20:03:25 2019

Challenge 2 : Change the Square class so that when you prnt  Square object, a message 
prints telling you the len of each of the four  sides of it's shape 


@author: zordo
"""

class Square():
    
    squares = []
        
    def __init__(self, l):
        self.lenght = l 
        self.squares.append(self.lenght)
        
    def calculate_perimeter(self):
        
        return (self.lenght * 4 )
    
    def __repr__(self):
        
        return (" {} by {} by {} by {}".format(self.lenght,self.lenght,self.lenght,self.lenght))
        
    
    


print(Square(29))    