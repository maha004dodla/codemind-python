a=input()
b=input()
a=a.lower()
b=b.lower()
a=list(a)
b=list(b)
l=[]
k=[]
for i in a:
    if i not in b and i!=' ':
        l.append(i)
for i in b:
    if i not in a and i!=' ':
        l.append(i)
c=list(set(l))
d=sorted(c)
e="".join(d)
print(e)