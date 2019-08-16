#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 21:46:09 2019

@author: zordo
"""

# Challenge 5 , write a program with a variable age assigined to an integer 
# that prints different strins depending on what the integer age is 


age = 70

if age < 18 :
    print("Child")

if age >=18  and age <= 25 :
    print("Young adult")
    
if age > 25 and age <= 65 :
    print("Adult")
    
if age > 65 :
    print (" Elderly ")    


    