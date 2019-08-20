#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 22:08:23 2019

Challenge 2 - Find a regular expression that matches all the digists in the strin

Arizona 49,501,870. California 209,213,650 

@author: zordo
"""


import re 

add = "Arizona 49,501,870. California 209,213,650"



me = re.findall('\d',add,re.IGNORECASE )


print(me)