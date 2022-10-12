n=int(input())
arr=list(map(int,input().split()))
l=[]
for i in arr:
    a=arr.count(i)
    if(a==1):
        flag=1
        l.append(i)
if(len(l)<1):
    print("-1")
else:
    print(max(l))
