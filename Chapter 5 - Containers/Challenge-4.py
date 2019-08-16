#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 23:24:20 2019

@author: zordo
"""

# Challenge 4 , write a program that lets the user ask your height , fav color
# and returns the result from the dictionary you created in the previous
# challenge 



my_dic = { "Eyes" : "Dark Brown" , "Height" : 1.81 ,"Weight" : "It's rude to ask :)","Age" : 23, "Occupation" : "Data Scientist" }


attribute = input("Ask something about me \n")


try :
    
    print(my_dic[attribute])
    
except KeyError:
    
    print("Enter a valid key, Eyes , Height , Weight, Age , Occupation . Case sensitive")