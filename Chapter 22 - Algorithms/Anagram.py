#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 00:59:29 2019


Anagram


@author: zordo
"""


    
def anagram(w1,w2):
        
    w1 = w1.lower()

    w2 = w2.lower()

    return sorted(w1) == sorted(w2)



print(anagram("iceman","cinema"))    





