s=input()
i,c=0,0
count=0
p=len(s)
while(p):
    if s[i]=="R":
        c=c+1
    else:
        c=c-1
    i=i+1
    if c==0:
        count=count+1
    p=p-1
print(count)