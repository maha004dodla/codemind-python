n=int(input())
arr=list(map(int,input().split()))
b=list(set(arr))
l=[]
for i in b:
    c=arr.count(i)
    if(c==i):
        l.append(i)
if(len(l)<1):
    print("-1")
else:
    print(min(l),max(l))