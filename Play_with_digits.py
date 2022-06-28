n=int(input())
a=list(map(int,input().split()))
sum=0
for i in range(n):
    while(a[i]):
        r=a[i]%10
        sum=sum+r
        a[i]=a[i]//10
print(sum)