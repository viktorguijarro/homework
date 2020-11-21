#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 21:35:34 2020

@author: viktor
"""

for x in range(100, 1000):
    a = x % 10
    b = ((x - a) / 10) % 10
    c = ((x - a) - (b * 10)) / 100
    if a == (b + c):
        print(x)
