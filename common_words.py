a=input()
b=input()
a=a.lower()
b=b.lower()
a=a.split(" ")
b=b.split(" ")
l=[]
for i in b:
    if i in a:
        l.append(i)
print(*l)