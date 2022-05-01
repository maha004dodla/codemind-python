n=int(input())
arr=list(map(int,input().split()))
count=0
count1=0
for i in range(n):
    if(arr[i]%2==0):
        count=count+1
for i in range(n):
    if(arr[i]%2!=0):
        count1=count1+1
print(count,count1)