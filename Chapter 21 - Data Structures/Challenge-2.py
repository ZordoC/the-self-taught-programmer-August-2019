#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 00:26:19 2019

Challenge 2 - Use a stack to create new list with items in the following list 
reversed [1,2,3,4,5]

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


for i in range(1,6):
    stack.push(i)
    
print(stack.items)


item = []

for i in range(stack.size()):
    item.append(stack.pop())


print(item)
    