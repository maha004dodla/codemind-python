n=int(input())
arr=list(map(int,input().split()))
sum=0
for i in range(n):
    a=arr[i]
    import math
    b=math.sqrt(a)
    c=round(b)
    sq=c*c
    if(a==sq):
        sum=sum+arr[i]
print(sum)
