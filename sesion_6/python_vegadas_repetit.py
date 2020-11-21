#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 15:17:10 2020

@author: viktor
"""

a=int(input(""))
b=int(input(""))
anterior=b
c=0
while b!=0:
    b=int(input(""))
    if b==a and b>=anterior:
        c=c+1
    anterior=b
print(c)