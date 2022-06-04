n=int(input())
arr=list(map(int,input().split()))
for i in range(len(arr)):
    if(arr[i]!=0):
        print(arr[i],end=" ")
for i in range(len(arr)):
    if(arr[i]==0):
        print(arr[i],end=" ")