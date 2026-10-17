nums=list(map(int, input().split()))
c=len(nums)
for i in nums:
     c=nums.count(i)
     if c>1:
      for j in range(len(range(c-1))):
          nums.remove(i)  
print(len(nums))
print(nums)