# -*- coding: utf-8 -*-
import sys
sys.stdin = open('square.in','r')
sys.stdout = open('square.out','w')

x1,y1,x2,y2 = [int(i) for i in input().split()]
x3,y3,x4,y4 = [int(i) for i in input().split()]

maxx = max(x1,x2,x3,x4) - min(x1,x2,x3,x4)
maxy = max(y1,y2,y3,y4) - min(y1,y2,y3,y4)
print(max(maxx,maxy)**2)

