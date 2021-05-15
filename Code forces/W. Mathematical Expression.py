# -*- coding: utf-8 -*-
sttr = input().split('=')
print('Yes' if str(eval(sttr[0])) == sttr[1].strip() else eval(sttr[0]))