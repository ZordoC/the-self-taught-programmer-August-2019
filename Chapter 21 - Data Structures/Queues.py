#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 23:52:39 2019

Queues

@author: zordo
"""

class Queue:
    
    def __init__(self):
        self.items = []
        
    
    
    def is_empty(self):
        return self.items == []
    
    def enqueue( self, item):
        self.items.insert(0,item)
        
        
    def dequeue(self):
        return self.items.pop()
    
    
    def size(self):
        
        return len(self.items)
    
        

a_queue = Queue()

print(a_queue.is_empty())  


for i in range(5):
    a_queue.enqueue(i)
    

for i in range(5):
    print(a_queue.dequeue())


print()


print(a_queue.size())


