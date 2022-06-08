n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
count=0
for i in range(n):
    c=0
    for j in range(m):
        if(a[i]==b[j]):
            b[j]=0
            c=c+1
    if(c!=0):
        count=count+1
print(count)