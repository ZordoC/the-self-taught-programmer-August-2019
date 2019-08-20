#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 19:45:57 2019

@author: zordo
"""


import re 


zen = """ Although never is often better than *right* now.
If the implementation is hard to explain,123 it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""


m = re.findall("\d",zen,re.MULTILINE)






print(m)


line = " I love you $" 

m =  re.findall("\\$", 
                line,
                re.IGNORECASE)


print(m)