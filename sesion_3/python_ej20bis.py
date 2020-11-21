#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 21:50:37 2020

@author: viktor
"""

n=int(input(""))
a=n
c=1
m=20000
while a<m:
    a=n**c
    c=c+1
print("",c-1)