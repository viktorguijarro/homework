#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 20:07:29 2020

@author: viktor
"""

a=int(input(""))
n=a
if n<=0:
    print("False")
else:
    h=0
    for i in range (0,n+1):
        for j in range (0,n-i):
            print(" ", end="")   
        for j in range(0,i+h-1):
            print("*", end="")
        print(end=" ")
        h=h+1
        print()