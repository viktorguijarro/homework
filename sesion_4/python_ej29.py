#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 21:03:28 2020

@author: viktor
"""

a=int(input(""))
n=a
b=0
c=1
if n<=0:
    print("False")
else:
    while c!=(n+1):
        b=b+(c*3)
        c=c+1
    print(b)