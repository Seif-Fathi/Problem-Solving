# -*- coding: utf-8 -*-
if __name__=='__main__':
    num_tsts = int(input())
    for i in range(num_tsts):
        sttr = input().lower()
        if len(sttr) <=10:
            print(sttr)
        else:
            print(sttr[0],len(sttr)-2,sttr[-1],sep='')
