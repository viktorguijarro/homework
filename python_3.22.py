#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 21:22:01 2020

@author: viktor
"""

def operacio (a,b,c):
    """
    """
    operacio=0
    if c=="+":
        operacio=a+b
    elif c=="/" and b!=0:
        operacio=a/b
    elif c=="*":
        operacio=a*b
    elif c=="-":
        operacio=a-b
    else:
        print("operacion no posible")
    return operacio

a=int(input(""))
b=int(input(""))
c=str(input(""))    
print(operacio (a,b,c))