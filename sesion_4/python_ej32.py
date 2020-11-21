#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 22:46:01 2020

@author: viktor
"""

a=int(input(""))
b=int(input(""))
n=a
m=b
if a==b:
    print(a)
elif a>b:
    while n>m:
        n=n-m
        if n==m:
            print(n)
        elif n<m:
            while n<m:
                m=m-n
                if n==m:
                    print(n)
elif a<b:
    while n<m:
        m=m-n
        if n==m:
            print(n)
        elif n>m:
            while n>m:
                n=n-m
                if n==m:
                    print(n)