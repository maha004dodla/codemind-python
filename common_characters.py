a=input()
b=input()
a=a.lower()
b=b.lower()
a=list(a)
b=list(b)
l=[]
k=[]
flag=0
for i in a:
    if i in b and i!=" ":
        l.append(i)
for i in b:
    if i in a and i!=" ":
        l.append(i)
for i in l:
    if i not in k:
        k.append(i)
        flag=1
c=sorted(k)
if(flag==1):
    print("".join(c))
else:
    print("-1")