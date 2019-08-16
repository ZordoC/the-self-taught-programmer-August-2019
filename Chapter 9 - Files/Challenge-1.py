#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 02:46:07 2019

@author: zordo
"""

# Challenge 1 - Find a file on your computer and print its content using python 


import os 

os.path.join("home","zordo","Documents","Projects","My_projects","Self Taught Programmer","Chapter 9 - Files/","hey.txt")

with open("hey.txt","r") as r:
    print(r.read())
