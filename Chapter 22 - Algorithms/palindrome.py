#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 00:57:50 2019

Palindrome

@author: zordo
"""

def palindrome(word):
    word = word.lower()
    return word[::-1] == word


print(palindrome("Mother"))


print(palindrome("Mom"))