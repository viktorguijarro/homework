#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 21:11:58 2020

@author: viktor
"""

a=int(input(""))
b=int(input(""))
c=int(input(""))
d=int(input(""))
e=(a+b+c+d)/4
f=0
numbers=[a,b,c,d]
for x in numbers:
    if x>e:
        f=f+1
print("", f)