#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 19:53:05 2020

@author: viktor
"""

a=int(input(""))
if a>10:
    b=a%10
    a=a-b
    a=a/10
    c=a%10
    if (c==7):
        print("True")
    else:
        print("False")
else:
    print("False")
