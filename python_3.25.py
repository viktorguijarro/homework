#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 20:00:04 2020

@author: viktor
"""

def aun_num_3 (a):
    """
    """
    b=0
    c=0
    while a>0:
        b=b+3
        c=c+b
        a=a-1
    return(c)
a=int(input(""))
c=aun_num_3 (a)
print(c)