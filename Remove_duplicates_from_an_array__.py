n=int(input())
arr=list(map(int,input().split()))
res = []
for i in arr:
    if i not in res:
        res.append(i)
        print(i,end=" ")