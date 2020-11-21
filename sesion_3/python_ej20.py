#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 22:14:53 2020

@author: viktor
"""

n=int(input(""))
a=n
c=1
m=20000
while a<m:
    count=c
    b=n
    while count>=1:
        b=b*n
        count=count-1
    a=b
    c=c+1
print(c)