# -*- coding: utf-8 -*-
def num_hist():
    symbol = input()
    num = int(input())
    numbers = input().split()
    lst = []
    for i in numbers:
        if i !=' ':
            lst.append(int(i))
    for i in range(len(lst)-1):
        print(symbol*lst[i])
    return symbol*lst[-1]
if __name__=='__main__':
    print(num_hist())