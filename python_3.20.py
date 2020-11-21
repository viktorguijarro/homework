#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 21:37:39 2020

@author: viktor
"""

def numero_cifras (a):
    """
    """
    n=a
    c=0
    while n>0:
        m=n%10
        n=(n-m)/10
        c=c+1
    return (c)
a=int(input(""))
c=numero_cifras (a)
print(c)