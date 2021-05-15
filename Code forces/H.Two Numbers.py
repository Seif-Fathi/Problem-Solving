# -*- coding: utf-8 -*-
import math
def floor(num1,num2):
    return 'floor {} / {} = {}'.format(num1,num2,int(num1/num2))
def ceil(num1,num2):
    return 'ceil {} / {} = {}'.format(num1,num2,math.ceil(num1/num2))
def round2(num1,num2):
    return 'round {} / {} = {}'.format(num1,num2,round(num1/num2+0.001))

a,b = map(int,input().split())
print(floor(a,b))
print(ceil(a,b))
print(round2(a,b))