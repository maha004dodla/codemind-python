n=int(input())
a=list(map(int,input().split()))
if(n%2==0):
    print(*a)
else:
    a.insert(n,0)
    print(*a)