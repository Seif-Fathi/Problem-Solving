n = int(input())*2
lst = [int(i) for i in input().split()]
num = 99999999999999

for i in range(n-1):
    for i2 in range(i+1,n):
        sum_ = 0
        nums = []
        
        for m in range(n):
            if m!=i2 and m!=i: nums.append(lst[m])
        nums = sorted(nums)
        
        for k in range(0,len(nums),2):
                sum_ += (nums[k+1] - nums[k])
       
        num = min(num,sum_)
        
print(num)