#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 20:38:34 2020

@author: viktor
"""

a=int(input(""))
b=int(input(""))
c=str(input(""))
if c!="+" and c!="-" and c!="*" and c!="/":
    print("")
else:
    if c=="+":
        d=a+b
    if c=="/":
        d=a/b
    if c=="*":
        d=a*b
    if c=="-":
        d=a-b
    print("",d)