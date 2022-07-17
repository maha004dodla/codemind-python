s=input()
s=s.lower()
s=s.split()
l=[]
for i in s:
    c=0
    for j in i:
        if j in 'aeiou':
            c+=1
    l.append(c)
m=max(l)
print(l.count(m))