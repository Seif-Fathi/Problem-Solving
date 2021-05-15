# -*- coding: utf-8 -*-
import math 
a,b,c,d = map(int,input().split())
print('YES' if math.log2(a) * b > math.log2(c) * d else 'NO')