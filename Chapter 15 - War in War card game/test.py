#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 18:38:35 2019

@author: zordo
"""

import Card as c 

import deck as d 

import game as g



card1 = c.Card(10,2)
card2 = c.Card(11,3)



print(card1 < card2)


print(card1 > card2)


print(card1)


# Deck test 

deck = d.Deck()
for card in deck.cards:
    print(card)
    
    
    
jogo = g.Game()

jogo.play_game()