# -*- coding: utf-8 -*-
import sys
sys.stdin = open('billboard.in','r')
sys.stdout = open('billboard.out','w')

x1, y1, x2, y2 = [int(i) for i in input().split()]
x3, y3, x4, y4 = [int(i) for i in input().split()]

covers = lambda p1, p2, pc1, pc2, pc3, pc4: p1 <= pc3 and p1 >=pc1  and p2 <=pc4 and p2 >= pc2
   
corners = 0

if covers(x1 ,y1 ,x3 ,y3 ,x4 ,y4): corners+=1 
if covers(x2 ,y1 ,x3 ,y3 ,x4 ,y4): corners+=1
if covers(x2 ,y2 ,x3 ,y3 ,x4 ,y4): corners+=1
if covers(x1 ,y2 ,x3 ,y3 ,x4 ,y4): corners+=1

if corners == 4: print(0)

elif corners <= 1: 
    x = max(x1,x2) - min(x1,x2)
    y = max(y1,y2) - min(y1,y2)
    print(x*y)
elif corners == 2:
    if covers(x1 ,y2 ,x3 ,y3 ,x4 ,y4) and covers(x1 ,y1 ,x3 ,y3 ,x4 ,y4):
       x = max(x1,x2) - max(x3,x4)
       y = max(y1,y2) - min(y1,y2)
    
    elif covers(x1 ,y2 ,x3 ,y3 ,x4 ,y4) and covers(x2 ,y2 ,x3 ,y3 ,x4 ,y4):
        x = max(x1,x2) - min(x1,x2)
        y = min(y3,y4) - min(y1,y2)
    
    elif covers(x2 ,y2 ,x3 ,y3 ,x4 ,y4) and covers(x2 ,y1 ,x3 ,y3 ,x4 ,y4):
         x = max(x3,x4) - min(x1,x2)
         y = max(y1,y2) - min(y1,y2)
         
    elif covers(x1 ,y1 ,x3 ,y3 ,x4 ,y4) and covers(x2 ,y1 ,x3 ,y3 ,x4 ,y4):
        x = max(x1,x2) - min(x1,x2)
        y = max(y1,y2) - max(y3,y4)
    print(x*y)