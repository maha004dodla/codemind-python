n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in a:
    if i in b:
        if i not in c:
            c.append(i)
print(*c)