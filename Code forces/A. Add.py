# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 22:04:47 2021

@author: seif
"""
def add(x,y):
    return x+y
if __name__ == '__main__':
    a,b = map(int,input().split())
    print(add(a,b))