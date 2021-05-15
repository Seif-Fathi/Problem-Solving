# -*- coding: utf-8 -*-
a,b,q = map(int,input().split())
if q%3==1:print(a)
    
elif q%3==2: print(b)

else: print(a^b)