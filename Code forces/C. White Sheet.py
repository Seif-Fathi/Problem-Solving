# -*- coding: utf-8 -*-
x1,y1,x2,y2 = [int(i) for i in input().split()]
x3,y3,x4,y4 = [int(i) for i in input().split()]
x5,y5,x6,y6 = [int(i) for i in input().split()]

area_wt = abs(x1-x2) * abs(y2-y1) 
area_bk = (abs(x6-x5) * abs(y6-y5)) + (abs(x4-x3) * abs(y3-y4))

def cvrd_crnr(w1,w2 ,b3,b4 ,b5,b6 ):
    num = 0
    if w1 <= b5 and w1 >=b3 and w2 <=b6 and w2 >= b4:num+=1
        
    return num 

bk1 = cvrd_crnr(x1,y1 ,x3,y3,x4,y4)
bk1+= cvrd_crnr(x1,y2,x3,y3,x4,y4)
bk1+= cvrd_crnr(x2,y1,x3,y3,x4,y4)
bk1+= cvrd_crnr(x2,y2,x3,y3,x4,y4)


if cvrd_crnr(x1,y1,x5,y5,x6,y6) != cvrd_crnr(x1,y1 ,x3,y3,x4,y4):
    bk2=cvrd_crnr(x1,y1,x5,y5,x6,y6)
else:bk2=0

if cvrd_crnr(x1,y2,x5,y5,x6,y6) != cvrd_crnr(x1,y2,x3,y3,x4,y4): bk2+=cvrd_crnr(x1,y2,x5,y5,x6,y6)
if cvrd_crnr(x2,y1,x5,y5,x6,y6) != cvrd_crnr(x2,y1,x3,y3,x4,y4): bk2+=cvrd_crnr(x2,y1,x5,y5,x6,y6)
if cvrd_crnr(x2,y2,x5,y5,x6,y6) != cvrd_crnr(x2,y2,x3,y3,x4,y4): bk2+=cvrd_crnr(x2,y2,x5,y5,x6,y6)

if bk1+bk2 >=4:
    if max(y1,y2) > max(y5,y6) and max(y1,y2) <= max(y3,y4):
        y_diff = y3 - y6  
        x_diff = 1
    elif max(y1,y2) > max(y3,y4) and max(y1,y2) <=max(y5,y6):
        y_diff = y5 - y4
        x_diff = 1
    elif max(x1,x2) > max(x6,x5) and max(x1,x2) <=max(x4,x3): 
        x_diff = x3-x6
        y_diff = 1
    elif max(x1,x2) < max(x6,x5) and max(x1,x2) > max(x3,y3): 
        x_diff = x5 - x4 
        y_diff = 1

if bk1 == 4 or bk1 == 3 or bk2 == 4 or bk2 == 3:print('NO')

elif bk1+bk2 >=4 and area_bk >=area_wt and y_diff <=0 :print('NO')

elif bk1+bk2 >=4 and area_bk >=area_wt and x_diff <=0 :print('NO')

else:print('YES')