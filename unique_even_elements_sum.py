n=int(input())
arr=list(map(int,input().split()))
b=set(arr)
c=list(b)
sum=0
for i in range(len(c)):
    if(c[i]%2==0):
        sum=sum+c[i]
print(sum)