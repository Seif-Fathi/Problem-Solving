# -*- coding: utf-8 -*-
import math
if __name__=='__main__':    
    num = int(input())
    test_num = math.log2(num)
    if int(test_num) == test_num :
        print('YES')
    else:
        print('NO')
