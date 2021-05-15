# -*- coding: utf-8 -*-
if __name__ == '__main__':
    num = int(input())
    lst = list(map(int,input().split()))
    lst2 = lst[::2]
    lst2.reverse() 
    print(*lst2)