# -*- coding: utf-8 -*-
import sys
sys.stdin = open('teleport.in','r')
sys.stdout = open('teleport.out','w')

a,b,x,y = [int(i) for i in input().split()]

way1 = max(a,b) - min(a,b)
way2 = abs(b - max(x,y)) + abs(a - min(x,y))
way3 = min( abs(b - x) , abs(b-y) ) + abs(a - min(x,y))   

if a == y and abs(b-x) < way1: print(abs(b-x))
else:print(min(way1,way2,way3))
 
