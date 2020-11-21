#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 20:05:43 2020

@author: viktor
"""

a=int(input(""))
n=a
if n<=0:
    print("False")
else:
    for i in range(2,int(n)+1):
        b=0
        for j in range (2,i):
            if i%j==0:
                b=1
        if b==0 and i!=n:
            print(i)