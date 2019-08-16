#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 19:46:18 2019

Challenge 1 -  Add a square_list to a class called Square so that every time 
you createa  new Square Object, the new object gets added to list 


@author: zordo
"""






class Square():
    
    squares = []
        
    def __init__(self, l):
        self.lenght = l 
        self.squares.append(self.lenght)
        
    def calculate_perimeter(self):
        
        return (self.lenght * 4 )

Square(2)
Square(4)
Square(5)
Square(7)
Square(3)

print(Square.squares)