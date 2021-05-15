# -*- coding: utf-8 -*-
n = list(map(int,input().split()))
for i in range(n[0]):
    sequence = input()
    lst = []
    a, b, c = 0, 1, 2
    e= False
    for i in sequence:
        lst.append(i)
        try:
            if '010' == lst[a]+lst[b]+lst[c] or '101' == lst[a]+lst[b]+lst[c] : 
                print('Good')
                e =True
                break
            else:
                a+=1
                b+=1
                c+=1
                continue
        except:
            continue
    if not e:
        print('Bad')