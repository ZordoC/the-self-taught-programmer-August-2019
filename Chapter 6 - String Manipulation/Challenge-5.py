#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 00:17:06 2019

@author: zordo
"""

#Challenge 5 TAke the list ["The","Fox","jumped","over","the","fence" "."], and 
# turn it into a grammatically correct string, there should be a space between
# each word but no space between thr word fence and the period that follows it .


string_l =  ["The","Fox","jumped","over","the","fence" ,"."]

one = " ".join(string_l)

print(one[:-2] + "." )

