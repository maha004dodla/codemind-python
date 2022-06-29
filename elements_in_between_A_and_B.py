n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
flag=0
for i in range(n):
    if(arr[i]>=a and arr[i]<=b):
        print(arr[i],end=" ")
        flag=1
if(flag==0):
    print("-1")