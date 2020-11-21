# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 20:22:37 2020

@author: vikto
"""


X=(-1)
Y=(10**100)
count=0
nunca_mas=0
contar=0
N=int(input())
while count<N:
    ant_X=X
    ant_Y=Y
    X=int(input())
    Y=int(input())
    count=count+1
    contar=contar+1
    if ant_X>X or ant_Y<Y and contar!=0:
        nunca_mas=nunca_mas+1
if nunca_mas>0:
    print(False)
else:
    print(True)