n=int(input())
arr=list(map(int,input().split()))
sum=0
for i in range(len(arr)):
    sum=sum+arr[i]
avg=sum//n
count=0
i=0
for i in range(n):
    if(arr[i]>=avg):
        count=count+1
print(count)