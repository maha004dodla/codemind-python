n=int(input())
arr=list(map(int,input().split()))
c=0
for i in range(0,n-2):
    if(arr[i]%2 and arr[i+1]%2 and arr[i+2]%2):
        c=c+1
print(c)