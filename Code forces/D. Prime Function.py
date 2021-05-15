# -*- coding: utf-8 -*-
def is_prime(num):
    if num <= 1 :
        return 'NO'
    if num <= 3:
        return 'YES'
    if num%2 == 0 or num%3 == 0:
        return 'NO'
    accum = 5
    while accum*accum <=num:
        if num%accum == 0 or num%(accum+2) == 0:
            return 'NO'
        accum += 6 
    return True

if __name__ == '__main__':
    num = int(input())
    for i in range(num):
        print(is_prime(int(input())))