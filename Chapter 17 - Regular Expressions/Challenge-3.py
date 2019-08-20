#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 22:17:19 2019

Create a regular expression that matches any word that starts with any charachter
and is followed by two o's. Then use Python re module to match boo and loo in the 
sentence: "The Ghost that syas boo haunts the loo, haunts the loo"

@author: zordo
"""




import re 



strings = "The Ghost that says boo haunts the loo"


print(re.findall('.oo',strings,re.IGNORECASE))