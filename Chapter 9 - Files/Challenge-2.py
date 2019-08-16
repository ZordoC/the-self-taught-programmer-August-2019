#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 02:49:44 2019

@author: zordo
"""

# Challenge 2-Write a program that asks a user a question and saves their answer
# to a file 


string = input("What's ya name , son ? \n ")

with open("hello.txt","w") as f:
    f.write(string)
        

with open("hello.txt","r") as r:
    print("\n You wrote this:")
    print(r.read())

