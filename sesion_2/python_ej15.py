#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 20:57:57 2020

@author: viktor
"""

a=str(input(""))
b=str(input(""))
c=str(input(""))
d=1
if a!=b and b!=c and a!=c:
    d=1
else:
    if a==b and b==c and a==c:
        d=3
    else:
        d=2
print("", d)