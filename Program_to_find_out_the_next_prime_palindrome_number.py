import math
def prime(p):
    if(p==1):
        return 0
    for i in range(2,int(math.sqrt(p)+1)):
        if(p%i==0):
            return 0
    else:
        return 1
def pal(q):
    a=str(q)
    b=a[::-1]
    if(a==b):
        return 1
    else:
        return 0
n=int(input())
nxt=n+1
while(nxt):
    if(prime(nxt)):
        if(pal(nxt)):
            print(nxt)
            break
    nxt+=1;