# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 20:02:16 2020

@author: vikto
"""


num=0
ant_1=0
count=0
posicion=0
while num>(-1):
    ant_2=ant_1
    ant_1=num
    num=int(input())
    despues=num
    posicion=posicion+1
    if ant_2<ant_1>num and posicion>=2 and num!=(-1):
        count=count+1
print(count)