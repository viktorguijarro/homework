#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 20:12:07 2020

@author: viktor
"""

a=int(input(""))
if a>99 and a<1000:
    primero=a%10
    a=a-primero
    a=a/10
    segundo=a%10
    tercero=(a-segundo)/10
    if (primero==tercero):
        print("True")
    else:
        print("False")
else:
        print("False")
