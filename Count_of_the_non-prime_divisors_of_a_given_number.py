import math
def prime(p):
    if(p==1):
        return 0
    for i in range(2,int(math.sqrt(p)+1)):
        if(p%i==0):
            return 0
    else:
        return 1
n=int(input())
l=[]
m=[]
c=0
for i in range(1,n+1):
    if(n%i==0):
        l.append(i)
for i in range(len(l)):
    if(prime(l[i])):
        m.append(l[i])
        c+=1
print(len(l)-c)