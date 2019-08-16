#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 03:40:13 2019

@author: zordo
"""

#Challenge 1 , modify the game so that a word is selected randomly from 
# a list of words 


from game import hangman
import random


words = ['Hello','dog','cat','bird','mouse','stone','puddle','cross','yellow','great','bingo','mobile','random']


word_ind = random.randint(0,len(words))



hangman(words[word_ind])