s=input()
s1=input()
s=list(s.lower())
s1=list(s1.lower())
a=[]
b=[]
flag=0
for i in s:
    if i not in s1 and (i!=' '):
            a.append(i)
for i in s1:
    if i not in s and (i!=' '):
            a.append(i)
for i in a:
    if i not in b:
        b.append(i)
print(len(b))
