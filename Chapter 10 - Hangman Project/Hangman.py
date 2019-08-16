#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 03:04:36 2019

@author: zordo
"""



def hangman(word):
    '''
    plays the game of hangman
    
    :param word: string for playing the game 
    
    
    '''
    
    
    wrong = 0
    
    stages = ["",
              "----------------                 ",
              "|                                ",
              "|               |                ",
              "|               O                ",
              "|              /|\               ",
              "|              / \               ",
              "|                                ",]
    
    rletters = list(word) # transforms words into a list of characthers
    board = ["_"] * len(word) # Creates a "board" list with the same size as the word but with _ to replace after every right guess
    
    print("Welcome to Hangman") # Welcome message 
    
    while wrong < len(stages) -1 : # Game repeats untill you ran out of lifes , this case is when the stages list is fully printed
        
        print("\n")
        msg = "Guess a letter \n"
        char = input(msg) # user inputs "guess" letter
        if char in rletters: # condition checks if the guess is within the word. 
            cind = rletters.index(char) # gets index of where the char is 
            board[cind] = char # replaces _ on the board with the correct guessed word.
            rletters[cind] = '$' # replaces the character guessed with $ so you don't guess again the same letter in the same position
            
        else :
            wrong += 1 # Registers a wrong guess
            print(" ".join(board)) 
            e = wrong + 1  
            print("\n".join(stages[0:e])) # prints the whole structure ! 
            if "_" not in board: # condition for win game 
                print("\n You win , nice job ! ")
                print(" ".join(board)) # spells the word with a space 
                win =  True # win 
                break
       
    if not win : # loose 
        print("\n".join(stages[0:wrong]))
        print("You lose ! It was {}.".format(word))
        
        

        
                
            

 

            
    
    