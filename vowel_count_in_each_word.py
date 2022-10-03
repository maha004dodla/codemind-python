s=input()
s=s.split()
a=[]
for i in s:
    c=0
    for j in i:
        if j in"aeiouAEIOU":
            c=c+1
    a.append(c)
print(*a)
        