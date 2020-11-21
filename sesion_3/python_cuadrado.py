#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 20:35:08 2020

@author: viktor
"""

def cuadrado(n):
    guess = n**(1.0/2.0)
    iguess = int(guess)
    if iguess * iguess == n:
        print(True)
        return
    iguess = iguess + 1
    if iguess * iguess == n:
        print(True)
        return
    print(False)
n = int(input(""))
cuadrado(n)