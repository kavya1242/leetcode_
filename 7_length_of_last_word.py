s=input()
s=s[::-1]
s=s.strip()                   
c=""                          
for i in s:                   
    if i==" ":                
        break                 
    else:                     
        c=c+i                 
print(len(c))                 