s=input()
b=len(s)
u=0
for i in range(0,b):
    ch=s[i]
    if(s[i]>='A' and s[i]<='Z'):
        u=u+1
print(u)