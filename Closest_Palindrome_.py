def pal(n):
    a=str(n)
    b=a[::-1]
    c=int(b)
    if(c==n):
        return True
    else:
        return False
n=int(input())
for i in range(n-1,-1,-1):
    if(pal(i)):
        bf=i
        break
s=n+1
while(1):
    if(pal(s)):
        af=s
        break
    s+=1
if(af-n==n-bf):
    print(bf,af)
elif(af-n<bf-n):
    print(af)
else:
    print(bf)