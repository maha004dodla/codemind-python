import math
def prime(p):
    if(p==1):
        return 1
    for i in range(2,int(math.sqrt(p)+1)):
        if(p%i==0):
            return 0
    else:
        return 1
n=int(input())
l=[]
for i in range(2,n):
    if(n%i==0):
        if(prime(i)):
            l.append(i)
if(len(l)==0):
    print(-1)
else:
    print(*l)