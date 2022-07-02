n=int(input())
arr=list(map(int,input().split()))
flag=0
for i in range(n):
    c=0
    for j in range(n):
        if(arr[i]==arr[j]):
            c=c+1
            if(i!=j):
                arr[j]=0
    if(arr[i]!=0):
        print(arr[i],c,end=" ")