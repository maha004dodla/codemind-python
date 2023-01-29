import math
def prime(p):
    if(p==1):
        return False
    for i in range(2,int(math.sqrt(p)+1)):
            if(p%i==0):
                return False
    else:
        return True
n=int(input())
arr=list(map(int,input().split()))
c=0
for i in range(0,n):
    if(prime(arr[i])):
        c+=1
print(c)

                