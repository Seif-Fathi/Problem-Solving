# -*- coding: utf-8 -*-
import sys
sys.stdin = open('speeding.in','r')
sys.stdout = open('speeding.out','w')

n,m = [int(i) for i in input().split()]
v_miles = []
for i in range(1,101):
    v_miles.append(i)
    
mile = 0
for i in range(n):
    lenght,limit = map(int,input().split())
    for num in range(lenght):
        v_miles[mile] = limit
        mile+=1

c_miles = []
for i in range(1,101):
    c_miles.append(i)

c_mile = 0
for i in range(m):
    lenght , limit = map(int,input().split())
    for num in range(lenght):
        c_miles[c_mile] = limit 
        c_mile+=1
        
over_limit = []
for i in range(100):
    if v_miles[i] < c_miles[i] : over_limit.append(c_miles[i] - v_miles[i])
    
print(max(over_limit) if over_limit != []  else 0 )