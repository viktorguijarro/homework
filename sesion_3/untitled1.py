#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 14:54:28 2020

@author: viktor
"""

import math
a=int(input(""))
n=a
if a<0:
    print("No")
else:
    if n > 0:
    digits = int(math.log10(n))+1
    elif n == 0:
    digits = 1
    else:
    digits = int(math.log10(-n))+2
