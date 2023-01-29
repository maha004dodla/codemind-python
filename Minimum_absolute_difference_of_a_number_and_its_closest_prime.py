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
for i in range(n,-1,-1):
    if(prime(i)):
        bf=i
        break
b=n+1
while(1):
    if(prime(b)):
        af=b
        break
    b+=1
A=abs(n-af)
B=abs(n-bf)
print(min(A,B))