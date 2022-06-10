n=int(input())
arr=list(map(int,input().split()))
temp=n-1
sum=0
for i in range(n):
    sum=sum+arr[i]*pow(2,temp)
    temp=temp-1
print(sum)