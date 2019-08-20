#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 22:42:00 2019

@author: zordo
"""

from flask import Flask


app = Flask (__name__)

@app.route('/')
def index():
    return "Hello World" 




app.run(port = '8000')