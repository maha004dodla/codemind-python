m,n=map(int,input().split())
l=[]
for i in range(0,m):
    d=0
    arr=list(map(int,input().split()))
    b=sorted(arr)
    c=b[::-1]
    if(arr==b or arr==c):
        d+=1
    l.append(d)
print(sum(l))