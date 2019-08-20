#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 23:38:38 2019

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
        
        last = len(self.items.pop())
        return self.items[last]
        
        
    def size(self):
        return len(self.items)



stack = Stack()



for i in range(0,6):
    stack.push(i)
    

print(stack.peek())


print(stack.size())

