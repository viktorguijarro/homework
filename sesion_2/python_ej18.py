#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 21:23:46 2020

@author: viktor
"""

import math
a=int(input(""))
b=int(input(""))
c=int(input(""))
d=(b**2)-(4*a*c)
if d<0:
    print("NO")
else:
    if d==0:
        e=(-b)/(2*a)
        print ("", e)
    else:
        e=((-b)-math.sqrt(d))/(2*a)
        f=((-b)+math.sqrt(d))/(2*a)
        print("",f,e)