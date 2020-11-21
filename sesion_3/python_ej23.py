#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 18:07:54 2020

@author: viktor
"""

def raiz_cuadrada (a):
    """
    """
    n=a
    m=n**(1/2)
    if (m%10)!=0:
        print("False")
    else:
        print("True")
    return (m)

a=int(input(""))
m=raiz_cuadrada (a)
print(m)