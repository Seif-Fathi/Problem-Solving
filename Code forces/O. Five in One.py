# -*- coding: utf-8 -*-
def is_prime(num):
    if num <= 1: return False
    if num <= 3: return True   
    if num%2 == 0 or num%3 == 0: return False
    accum = 5
    while accum*accum <=num:
        if num%accum == 0 or num%(accum+2) == 0: return False
        accum += 6 
    return True

input()
array = list(map(int,input().split()))
print('The maximum number : {}'.format(max(array)))
print('The minimum number : {}'.format(min(array)))

primes = 0
palindromes = 0

for i in array:
    if is_prime(i): primes+=1    
    if str(i)[:] == str(i)[::-1]: palindromes+=1
              
print('The number of prime numbers : {}'.format(primes))
print('The number of palindrome numbers : {}'.format(palindromes))

dic = {}
for i in array:
    accum = 0
    for k in range(1,i+1):
        if is_prime(i):
            dic[str(i)]=2
            break
        elif i%k==0: accum+=1
    if not is_prime(i): dic[str(i)] = accum      
        
st = []
for i in dic.keys():
	if dic[i] == max(dic.values()):st.append(int(i))
	else:continue
	    
print('The number that has the maximum number of divisors : {}'.format(max(st)))