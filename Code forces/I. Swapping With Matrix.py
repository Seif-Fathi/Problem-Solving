# -*- coding: utf-8 -*-
nums = [int(i) for i in input().split()]
t_lst = []
for i in range(nums[0]):
    array = [int(i) for i in input().split()]
    t_lst.append(array)
    t_lst[i][nums[1]-1] , t_lst[i][nums[2]-1] = t_lst[i][nums[2]-1] , t_lst[i][nums[1]-1]
t_lst[nums[2]-1] , t_lst[nums[1]-1] = t_lst[nums[1]-1] , t_lst[nums[2]-1]
for i in t_lst:
    print(*i)