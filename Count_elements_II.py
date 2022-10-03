m,n=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
d=[]
for i in a:
   if i not in b:
       c.append(i)
for i in b:
    if i not in a:
        c.append(i)
for i in c:
    if i not in d:
        d.append(i)
print(len(d))
