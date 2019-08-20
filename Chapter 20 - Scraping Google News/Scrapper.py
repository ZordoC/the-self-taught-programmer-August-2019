#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 22:56:27 2019

@author: zordo
"""

import urllib.request
from bs4 import BeautifulSoup




class Scraper:
    
    def __init__(self,site):
        self.site = site
        
        
        
    def scrape(self):
        buffer = []
        r =  urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        
        for tag in sp.find_all("a"):
            
            url = tag.get('href')
            if url is None :
                continue
            
            if "html" in url:
                print("\n" + url)
                buffer.append(url)
                
            
        with open('file.txt', 'w') as f:
            for item in buffer:
                f.write("%s\n" % item)    
        
       
       
            
            
                      
    

news = 'https://en.wikipedia.org/wiki/Super_Mario'

Scraper(news).scrape()