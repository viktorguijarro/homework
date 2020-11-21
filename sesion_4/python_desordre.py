#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 20:21:50 2020

@author: viktor
"""

a=int(input(""))
n=a+1
if n<=0:
    print("False")
else:
    for i in range (1,n+1):
        n=n-1    
        if n>=i:
            print(i)
        if n>i:
            print(n)