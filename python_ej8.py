#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 19:16:36 2020

@author: viktor
"""

a=int(input("Entra un numero: "))
b=int(input("Entra un numero: "))
if ((a%b==0) or (b%a==0)) and ((b!=0) and (a!=0)):
    print("True")
else:
    print("False")