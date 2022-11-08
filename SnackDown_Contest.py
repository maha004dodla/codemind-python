n=int(input())
for i in range(n):
    m=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    l=[]
    for i in a:
        l.append(i)
    for j in b:
        l.append(j)
    c=len(set(l))
    if(c==m):
        print("YES")
    else:
        print("NO")
        