nums1=list(map(int, input().split()))
nums2=list(map(int, input().split()))
a=sorted(nums1+nums2)
n=len(a)
m=n//2

if  len(a)%2!=0:
    print(float(a[m]))
else:
    print(float(a[m]+a[m-1])/2)
