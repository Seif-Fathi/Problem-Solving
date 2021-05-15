# -*- coding: utf-8 
def is_prime(num):
    if num> 1:
        for i in range(2,num):
            if num%i == 0:
                return 'NO'
    return 'YES'
 
print(is_prime(int(input())))

