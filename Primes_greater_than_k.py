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
arr=list(map(int,input().split()))
k=int(input())
c=0
l=[]
for i in range(n):
    if(prime(arr[i])):
        l.append(arr[i])
for i in l:
    if(i>=k):
        c+=1
print(c)