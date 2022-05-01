n=int(input())
arr=list(map(int,input().split()))
k=int(input())
count=0
for i in range(n):
    if(arr[i]==k):
        count=count+1
print(count)