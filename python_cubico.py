#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 19:34:38 2020

@author: viktor
"""

def is_cube(n):
    guess = n**(1.0/3.0)
    iguess = int(guess)
    if iguess * iguess * iguess == n:
        print(True, "it's cubed root is", iguess)
        return
    iguess = iguess + 1
    if iguess * iguess * iguess == n:
        print(True, "it's cubed root is", iguess)
        return
    print(False, "it's cubed root is", guess)
n = int(input(""))
is_cube(n)