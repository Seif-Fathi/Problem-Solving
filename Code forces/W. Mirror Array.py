# -*- coding: utf-8 -*-
r,c = map(int,input().split())
for i in range(r):
    print(*list(map(int,input().split()))[::-1])

