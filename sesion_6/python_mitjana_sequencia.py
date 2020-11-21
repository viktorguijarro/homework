# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 08:49:47 2020

@author: vikto
"""


x=int(input())
s=0
n=0

while (x!=0):
  s=s+x
  n=n+1
  x=int(input())
if n>0:
    m=(s/n)
else:
    m=0
print(m)