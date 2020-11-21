#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 19:29:26 2020

@author: viktor
"""

def funcion_compuesta (a,b):
    """
    """
    m=0
    if a>b:
        m=a%b+1
    elif a<b:
        m=b%a
    else:
        m=1.0
    return (m)
a=int(input(""))
b=int(input("")) 
m=funcion_compuesta(a,b)   
print(m)