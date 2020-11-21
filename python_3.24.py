#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 22:10:02 2020

@author: viktor
"""

def divisores (a):
    """
    """
    n=a
    for i in range(1,n+1):
         if n%i==0:
             print (i)
    return (i)
a=int(input(""))
i=divisores (a)