a,b=map(int,input().split())
arr=list(map(int,input().split()))
c=arr[:b]
d=arr[b:]
print(*d,end=" ")
print(*c)