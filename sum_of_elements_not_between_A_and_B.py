n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
sum=0
for i in range(n):
    if(arr[i]<a or arr[i]>b):
        sum=sum+arr[i]
print(sum)