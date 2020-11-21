# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 20:48:49 2020

@author: vikto
"""


count=1
num=int(input())
while num!=0:
    ant_num=num
    num=int(input())
    if ant_num==num:
        count=count+1
    else:
        print("(",ant_num,":",count,") ")
        count=1
        ant_num=num

        
