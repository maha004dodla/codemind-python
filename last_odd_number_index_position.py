n=int(input())
arr=list(map(int,input().split()))
c=0
for i in range(n-1,1,-1):
    if(arr[i]%2!=0):
        print(i)
        break