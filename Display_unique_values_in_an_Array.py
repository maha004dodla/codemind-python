n=int(input())
arr=list(map(int,input().split()))
flag=0
for i in range(n):
    count=0
    for j in range(n):
        if(arr[i]==arr[j]):
            count=count+1
    if(count==1):
        flag=1
        print(arr[i],end=" ")
if(flag==0):
    print("-1")