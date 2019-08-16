#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 02:56:32 2019

@author: zordo
"""

# Challenge 3 - Take the items in this list of lists [["Top gun","Risky Business","Minority Report"], ["Titanic","The revenant","Inception"],
#["Training Day","Man on Fire","Flight"]]


movies = [["Top gun","Risky Business","Minority Report"], 
          ["Titanic","The revenant","Inception"],
          ["Training Day","Man on Fire","Flight"]]


import csv 

with open("movies.csv","w", newline = '') as f:
    w =  csv.writer(f, delimiter = ",")
    
    for i, mov in enumerate(movies):
        w.writerow(movies[i])
 
    
    