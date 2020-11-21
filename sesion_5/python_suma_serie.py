#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 21:29:34 2020

@author: viktor
"""

def factorial(a):
    b=1
    while a!=0:
        b=b*a
        a=a-1
    return b
n=int(input(""))
x=float(input(""))
sum=0
e=0
for i in range (0,n+1):
    e=(x+2*i)/(factorial(i))
    sum=sum+e
print(sum)