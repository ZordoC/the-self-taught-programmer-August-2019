#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 00:34:38 2019

@author: zordo
"""

#Challenge 10 - SLice the strin "It was a bright cold day in Aprikl, and the
#clocks were strinking thirteen." to only include the charcthers before the comma

string = "It was a bright cold day in April, and the clocks were strinking thirteen"

print(string[:string.index(',')])