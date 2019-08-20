#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 19:40:10 2019

@author: zordo
"""

import re 


l = "Beautiful is better than ugly" 


matches = re.findall("Beautiful",l)

matchess = re.findall("beautiful",l,re.IGNORECASE)

print(matches)

print("\n")

print(matchess)