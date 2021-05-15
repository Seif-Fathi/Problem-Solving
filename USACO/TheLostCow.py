# -*- coding: utf-8 -*-
import sys
sys.stdin = open('lostcow.in','r')
sys.stdout = open('lostcow.out','w')

x,y = [int(i) for i in input().split()]
num = 1
moves = 0

if y > x:
    for i in range(x*9):
        for k in range(1):
            try:
                moves+=abs(pos-x)
            except NameError:pass
            pos=x+num
            if pos>=y:
                moves+=abs(y-x)
                break
            moves+=abs(pos-x)
            num*=2
        if pos >=y :break
        for n in range(1):
            moves+=abs(pos-x)
            pos= x-num
            moves+=abs(pos-x)
            num*=2
            
else:
    for i in range(x*9):
        for k in range(1):
            try:
                moves+=abs(pos-x)
            except NameError:pass
            pos = x+num 
            moves+=abs(pos-x)
            num*=2
        for n in range(1):
            moves+=abs(pos-x)
            pos = x-num 
            if pos<=y:
                moves+=abs(y-x)
                break
            moves +=abs(pos-x)
            num*=2
        if pos<=y:break
       
print(moves)