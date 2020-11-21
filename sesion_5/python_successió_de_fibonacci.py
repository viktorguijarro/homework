#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 23:16:13 2020

@author: viktor
"""

a=int(input(""))
if a>0:
    print(1)
    x,y=0,1
    while y<=a:
        x,y = y,x+y
        if y<a:
            print(y)
else:
    print("False")