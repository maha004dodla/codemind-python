n=int(input())
arr=list(map(int,input().split()))
es=0
os=0
for i in range(n):
    if(i%2==0):
        es=es+arr[i]
    if(i%2!=0):
        os=os+arr[i]
a=es-os
print(a)
