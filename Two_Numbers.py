n=int(input())
arr=list(map(int,input().split()))
l=[]
for i in arr:
    a=arr.count(i)
    if(a==1):
        l.append(i)
l=sorted(l)
print(*l)