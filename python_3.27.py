#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 20:33:36 2020

@author: viktor
"""

def raiz_cubica (a):
    """
    """
    n=a
    m=n**(1/3)
    if (m%10)!=0:
        print("False")
    else:
        print("True")
    return (m)

a=int(input(""))
m=raiz_cubica (a)
print(m)