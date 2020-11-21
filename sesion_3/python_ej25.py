#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 18:20:15 2020

@author: viktor
"""

def contar_digito (a):
    """
    """
    m=0
    while a>0:
        b=a%10
        a=a//10
        if b==c:
            m=m+1
    return (m)
a=int(input(""))
c=int(input(""))
m=contar_digito (a)
print(m)