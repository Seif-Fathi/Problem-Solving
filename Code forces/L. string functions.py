# -*- coding: utf-8 -*-
  
nums,queries= map(int, input().split())
sttr = input()

for i in range(queries):
    user_input = input().split()
    if user_input[0] == "pop_back":
        sttr = sttr[:-1]
        
    elif user_input[0] == "front":
        print(sttr[0])
        
    elif user_input[0] == "back":
        print(sttr[-1])
        
    elif user_input[0] == "sort":
        l = min(int(user_input[1]),int(user_input[2]))
        r = max(int(user_input[1]),int(user_input[2]))
        sttr = sttr[:l-1] + ''.join(sorted(sttr[l-1:r])) + sttr[r:]
        
    elif user_input[0] == "reverse":
        l = min(int(user_input[1]),int(user_input[2]))
        r = max(int(user_input[1]),int(user_input[2]))
        sttr = sttr[:l-1] + sttr[l-1:r][::-1] + sttr[r:]
        
    elif user_input[0] == "print":
        pos = int(user_input[1]) - 1
        print(sttr[pos])
        
    elif user_input[0] == "substr":
        l = min(int(user_input[1]),int(user_input[2]))
        r = max(int(user_input[1]),int(user_input[2]))
        print(sttr[l-1:r])
        
    elif user_input[0] == "push_back":
        sttr = sttr + user_input[1]