n=int(input())
arr=list(map(int,input().split()))
l=[]
for i in arr:
    a=abs(i)
    b=len(str(a))
    l.append(b)
print(*l)