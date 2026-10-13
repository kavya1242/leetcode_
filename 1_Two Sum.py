'''nums=[3,3]
target=6
c=[]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            c.append(i)
            c.append(j)

print(c)'''
#optimal
nums=[2, 7, 11, 15]
target=9
seen = {}
for i, num in enumerate(nums):
    diff = target - num
    if diff in seen:
      print([seen[diff], i])
      
    seen[num] = i