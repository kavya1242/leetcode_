x=int(input())
sign=-1 if x<0 else 1
rev=0
x=abs(x)
while x!=0:
    lastdigit=x%10
    rev=(rev*10)+lastdigit
    x=x//10
rev=rev*sign
if rev==x and rev>0:
    print(True)
else:
    print(False)

