n,k=map(int,input().split())
arr=list(map(int,input().split()))
l=[]
for i in arr:
    b=abs(i)
    a=len(str(b))
    l.append(a)
b=l.count(k)
print(b)