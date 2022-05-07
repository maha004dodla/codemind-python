s=input()
b=len(s)
l=0
for i in range(0,b):
    ch=s[i]
    if(s[i]>='a' and s[i]<='z'):
        l=l+1
print(l)