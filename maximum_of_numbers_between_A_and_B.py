n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
l=[]
for i in range(n):
    if(arr[i]>=a and arr[i]<=b):
        l.append(arr[i])
if(len(l)<1):
    print("-1")
else:
    print(max(l))