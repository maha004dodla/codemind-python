n=int(input())
arr=list(map(int,input().split()))
c=[]
for i in arr:
    b=arr.count(i)
    if(i not in c):
        c.append(i)
print(*c)