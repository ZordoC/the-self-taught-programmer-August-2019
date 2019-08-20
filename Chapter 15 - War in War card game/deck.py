#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 18:40:33 2019

@author: zordo
"""

from random import shuffle 
import Card as c 

class Deck:
    
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(c.Card(i,j))
        
        shuffle(self.cards)
        
        
        
    def rm_card(self):
        if len(self.cards) == 0:
            return 
        return self.cards.pop()
    
    