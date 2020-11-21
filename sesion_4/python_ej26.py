#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 21:25:29 2020

@author: viktor
"""

a=int(input(""))
n=a
if n<=0:
    print("False")
else:
    for m in range(n+1,1,-1):
        b=0
        for x in range (1,m):
            b= b + x
        print (b)