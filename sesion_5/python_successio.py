#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 23:28:01 2020

@author: viktor
"""

n=int(input(""))
x=float(input(""))
a=0
b=0
for i in range (0,n):
    a=pow(x,i)/pow(2,i)
    b=b+a
print(b)