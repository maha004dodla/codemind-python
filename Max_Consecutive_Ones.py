n=int(input())
arr=list(map(int,input().split()))
c=0
max=0
for i in range(n):
    if(arr[i]==1):
        c=c+1
    if(arr[i]==0):
        if(max<c):
            max=c
        c=0
if(max<c):
    max=c
print(max)