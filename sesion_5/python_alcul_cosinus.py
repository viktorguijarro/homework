#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 23:41:58 2020

@author: viktor
"""

def factorial(a):
    b=1
    while a!=0:
        b=b*a
        a=a-1
    return b
x=float(input(""))
n=int(input(""))
f=0
m=0
t=0
for i in range (0,n+1,2):
    m=pow(x,i)/factorial(i)
    t=t+1
    if t/2==int:
        f=f+m
    else:
        f=f-m
print(f)