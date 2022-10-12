a,b=map(int,input().split())
arr=list(map(int,input().split()))
brr=list(map(int,input().split()))
arr=set(arr)
brr=set(brr)
m=sorted(list(arr))
n=sorted(list(brr))
c=0
for i in m:
    if i in n:
        c+=1
print(c)
