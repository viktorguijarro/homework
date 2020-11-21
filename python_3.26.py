#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 21:07:55 2020

@author: viktor
"""

def contar_digito (a):
    """
    """
    m=0
    while a>0:
        b=a%10
        a=a//10
        if b==7:
            m=m+1
    return (m)
a=int(input(""))
m=contar_digito (a)
print(m)