m,n=map(int,input().split())
l=[]
for i in range(0,m):
    arr=list(map(int,input().split()))
    l.append(arr)
for i in range(0,m):
    m=0
    for j in range(0,n):
        if(l[j][i]>m):
            m=l[j][i]
    print(m)