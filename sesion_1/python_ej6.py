#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 17:57:37 2020

@author: viktor
"""

a=int(input(""))
if ((a!=1) and (a!=3) and (a!=5) and (a!=7) and ((a%3==0) or (a%5==0) or (a%7==0) or (a%9==0))):
    print("True")
else:
    print("False")
