# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 09:15:43 2020

@author: vikto
"""


x=int(input())
maxim=x
minim=x

while x!=0:
    if x>maxim:
        maxim=x
    if x<minim:
        minim=x
    x=int(input())
print(maxim)
print(minim)
