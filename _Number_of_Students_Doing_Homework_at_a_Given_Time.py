m=int(input())
a=list(map(int,input().split()))
n=int(input())
b=list(map(int,input().split()))
o=int(input())
c=0
for i in range(m):
    if(o>=a[i] and o<=b[i]):
        c+=1
print(c)

