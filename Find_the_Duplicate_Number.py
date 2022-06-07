n=int(input())
arr=list(map(int,input().split()))
b=[]
for i in arr:
    a=arr.count(i)
    if i not in b and a>1:
        b.append(i)
print(*b)