n=int(input())
arr=list(map(int,input().split()))
l=[]
for i in arr:
    a=str(i)
    b=a[::-1]
    c=int(b)
    l.append(c)
print(*l)