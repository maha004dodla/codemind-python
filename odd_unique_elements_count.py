n=int(input())
arr=list(map(int,input().split()))
b=set(arr)
c=list(b)
count=0
for i in range(len(c)):
    if(c[i]%2!=0):
        count=count+1
print(count)