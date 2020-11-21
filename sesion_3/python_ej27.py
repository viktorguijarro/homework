#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 20:40:20 2020

@author: viktor
"""

n = int(input(''))
reversed = 0
	
while(n!=0):
	r=int(n%10)
	reversed = reversed*10 + r
	n=int(n/10)
		
print(reversed)