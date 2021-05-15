import sys
sys.stdin = open('cowsignal.in','r')
sys.stdout = open('cowsignal.out','w')

m,n,k = map(int,input().split())

for i in range(m):
    x = input()
    for n in range(k):
       print(''.join([i*k for i in x]))
    

