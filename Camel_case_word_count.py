s=input()
count=1
for i in range(1,len(s)):
     if(ord(s[i])<=91 and ord(s[i])>=65):
        count+=1
print(count)