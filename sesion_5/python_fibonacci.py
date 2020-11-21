#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 15:43:40 2020

@author: viktor
"""

a=int(input(""))
b=int(input(""))
if 2<=a<=b:
    x,y=0,1
    sum=0
    while y<=b:
        if y>=a:
            sum=sum+y
        x,y = y,x+y
else:
    print("False")
print(sum)