n=int(input())
a=list(map(int,input().split()))
s=""
for i in a:
    s+=str(i)
b=int(s)+1
c=str(b)
l=[]
for i in c:
    l.append(i)
print(*l)