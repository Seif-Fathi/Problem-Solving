# -*- coding: utf-8 -*-
if __name__=='__main__':
    sttr = input().lower()
    if sttr[::-1] == sttr[:]:
        print('YES')
    else:
        print('NO')
