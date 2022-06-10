n=int(input())
arr=list(map(int,input().split()))
for i in range(n):
    c=0
    for j in range(0,n):
        if(arr[i]>arr[j]):
            c=c+1
    print(c,end=" ")