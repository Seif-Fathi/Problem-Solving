# -*- coding: utf-8 -*-
if __name__ == '__main__':
    num_str = input()
    lst = []
    for i in num_str:
        lst.append(int(i))
    if lst[0]%2 == 0:
        print('EVEN')
    else:
        print('ODD')
