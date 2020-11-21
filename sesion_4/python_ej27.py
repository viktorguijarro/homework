#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 18:11:14 2020

@author: viktor
"""

a=int(input(""))
n=a
b=0
if n<=0:
    print("False")
else:
    while n>=0:
        b=b+n
        n=n-1
    print(b)