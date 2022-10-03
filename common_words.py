s=input()
s1=input()
s=s.lower()
s1=s1.lower()
s=s.split(" ")
s1=s1.split(" ")
a=[]
for i in s1:
    if i in s:
        if i not in a:
            a.append(i)
print(*a)