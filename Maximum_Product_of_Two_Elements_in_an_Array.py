arr=list(map(int,input().split()))
a=sorted(arr)
n=len(a)
b=a[n-1]
c=a[n-2]
print((b-1)*(c-1))