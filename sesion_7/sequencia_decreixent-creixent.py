# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 09:13:22 2020

@author: vikto
"""


N=input()
x=int(input())
y=int(input())
c= False
d= False
while len(x)!=N and len(y)!=N:
    for i in x:
        if x[i]<x[i+1]:
            c= True
        if y[i]>y[i+1]:
            d=True
    x=int(input())
    y=int(input())
print(c==d)