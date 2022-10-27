n=int(input())
arr=list(map(int,input().split()))
b=int(input())
if b not in arr:
    print("-1 -1")
c=arr.index(b)
arr.reverse()
d=arr.index(b)
e=(n-d)-1
print(c,e)

