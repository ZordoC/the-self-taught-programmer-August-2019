#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 00:36:43 2019

FizzBuzz Algorithm- prints numbers 1 through 100 , for multiples of three 
print "Fizz"  and for multiple of 5 print "Buzz" for multiples of both 3 and 
5 prinnt FizzBuzz

@author: zordo

"""


def fizz_buzz():
    
    for i in range(1,101):
        if i % 3 == 0:
            print('Fizz')
        
        
        if i % 5 == 0:
            print('Buzz')
            
        
        if i % 5 == 0 and i % 3 == 0 :
            print('FizzBuzz')
        
        
        else:
            print(i)
    


fizz_buzz()

     
        