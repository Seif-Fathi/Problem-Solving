# -*- coding: utf-8 -*-
if __name__=='__main__':
    lst = list(map(int,input().split()))
    strr = input()
    num = 0
    for i in strr:
        if i == '-':
            num+=1
    try:
        if strr.index('-') == lst[0] and len(strr) == lst[0] + lst[1] + 1 and num == 1:
            print('Yes')
        else:
            print('No')
    except:
        print('No')