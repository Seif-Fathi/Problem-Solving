# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 02:18:33 2021

@author: seif
"""

if __name__ == '__main__':
    input()
    lst_2 = []
    lst_1= input().split()
    for i in lst_1:
        i = int(i)
        if i > 0:
            i= 1
            lst_2.append(i)
        elif i == 0:
            lst_2.append(i)
        else:
            i= 2
            lst_2.append(i)
    print(*lst_2)
            