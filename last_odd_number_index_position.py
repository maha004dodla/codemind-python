n=int(input())
arr=list(map(int,input().split()))
for i in range(n):
    arr[i]=arr[n-1]
    if(arr[i]%2!=0):
        b=i
print(b)