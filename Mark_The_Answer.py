n,m=map(int,input().split())
arr=list(map(int,input().split()))
c=0
for i in arr:
    if(i>=m):
        c+=1
print(c)