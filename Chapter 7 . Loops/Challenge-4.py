#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 01:00:54 2019

@author: zordo
"""

#Challenge 4 - Write a program with an infinite loop( with the option to tupe q to quit) and 
# and a list of numbers. Each time Through the loop ask the user to guess a number
#on the list and tell them wether or not they guessed correctly


 
nums2 = [i for i in range(1,5) ]

  

while (input("Press q to quit \n ") != 'q'): 
    
    
    if int(input("Guess a number \n ")) in nums2:
        
        print("Congrats you guessed right , here's a cookie you silly human !! ")
    
    
    else: print("Sorry ... Try again \n")    