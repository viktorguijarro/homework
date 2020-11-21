#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 18:01:48 2020

@author: viktor
"""

def suma_cifras (a):
    """
    """
    m=0
    while a>0:
        b=a%10
        m=m+b
        a=(a-b)/10
    return (int(m))
a=int(input(""))
m= suma_cifras (a)
print(m)