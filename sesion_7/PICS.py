# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 09:00:33 2020

@author: vikto
"""


x = int(input())
n = 0
y = int(input())
z = int(input())

while z!=-1:
    x = y
    y = z
    z = int(input())
    if y<x and x>z or y<z and z>x:
        n = n+1
print(n)