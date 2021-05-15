# -*- coding: utf-8 -*-:
import sys
sys.stdin = open('buckets.in','r')
sys.stdout = open('buckets.out','w')

for i in range(10):
    s = input()
    if 'B' in s: 
        b = i
        xb = s.index('B') 
    if 'R' in s: 
        r = i
        xr= s.index('R')
    if 'L' in s: 
        l = i
        xl = s.index('L')
    if 'B' in s and 'L' in s and 'R' in s: 
        true = 1
        break
    else: true = 0

x_diff = abs(xb-xl)
   
if xr == xl and xr == xb and r > min(b,l) and r < max(b,l):print(abs(b-l) + 1)
elif true == 1 and xr < max(xl,xb) and xr > min(xb,xl): print(x_diff + 1)
else:print(abs(b-l)+ x_diff-1)