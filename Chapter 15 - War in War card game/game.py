#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 18:00:08 2019

@author: zordo
"""

import deck as d 

import player as p


class Game:
    
    def __init__(self):
        name1 = input("p1 name")
        name2 = input("p2 name")
        self.deck = d.Deck()
        self.p1 = p.Player(name1)
        self.p2 = p.Player(name2)
        
        
    def wins(self,winner):
        w = "{} wins this round"
        w = w.format(winner)
        print(w)
        
        
        
    def draw(self,p1n,p1c,p2n,p2c):
        d = "{} drew {} {} drew {}"
        d = d.format(p1n,p1c,p2n,p2c)
        print(d)
        
        
        
    def play_game(self):
        cards = self.deck.cards
        print("Let the War Games Begin")
        while len(cards) >= 2:
            m = "q to quit. Any  " + "key to play:" 
            response = input(m)
            if response == 'q':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name 
            self.draw(p1n, p1c , p2n , p2c ) 
                
            if p1c > p2c:
                    
                self.p1.wins +=1 
                self.wins(self.p1.name)
                    
            else:
                self.p2.wins += 1 
                self.wins(self.p2.name)
                    
                    
                    
        win = self.winner(self.p1,self.p2)
        
        print("War is over. {} wins ".format(win))



    def winner(self,p1,p2):
        
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name 
        
        return "It was a tie " 
    
    
    


                        
                    
                    
                    
                
                
        