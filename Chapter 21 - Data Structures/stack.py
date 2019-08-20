#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 23:38:38 2019

Stack

@author: zordo
"""

class Stack:
    
    def __init__(self):
        self.items = []
        
        
    def is_empty(self):
        return self.items == []
    
    
    def push(self, item):
        self.items.append(item)
    
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        
        last = len(self.items) -1 
        return self.items[last]
        
        
    def size(self):
        return len(self.items)



stack = Stack()


# push and pop 

print(stack.is_empty())

stack.push(2)

item = stack.pop()

print(item)

print(stack.is_empty())


## peeking and size

for i in range(0,6):
    stack.push(i)
    

print(stack.peek())


print(stack.size())

#Reversing a string with a Stack


stack_2 = Stack()

for c in "Hello":
    stack_2.push(c)



    
reverse = ""




for i in range(len(stack_2.items)):
    reverse += stack_2.pop()


 
print(reverse)





