#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 16:14:31 2020

@author: viktor
"""

a=int(input(""))
b=float(input(""))
n=a
x=b
if n<=0:
    print("False")
else:
    for k in range(0,n+1):
        def factorial(k):
            if k==0:
                return 1
            else:
                return k*factorial(k-1)
        c=(x+2*k)/(k*factorial(k-1))
    print(c)