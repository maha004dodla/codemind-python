a=input()
b=input()
a=a.lower()
b=b.lower()
a=list(a)
b=list(b)
l=[]
k=[]
for i in a:
    if i in b and i!=" ":
        l.append(i)
for i in b:
    if i in a and i!=" ":
        l.append(i)
for i in l:
    if i not in k:
        k.append(i)
m="".join(k)
a=set(m)
print(len(a))
