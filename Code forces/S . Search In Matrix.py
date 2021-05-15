# -*- coding: utf-8 -*-

r , c = map(int,input().split())
str_nums = [str(i) for k in [input().split() for m in range(r)] for i in k]
print("will take number" if input() not in str_nums else "will not take number")
  

