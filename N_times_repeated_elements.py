n=int(input())
arr=list(map(int,input().split()))
c=int(input())
flag=0
for i in range(n):
    count=0
    for j in range(0,n):
        if(arr[i]==arr[j]):
            count=count+1
    if(count==c):
        flag=1
        print(arr[i],end=" ")
        arr[i]=-1
if(flag==0):
    print("-1")