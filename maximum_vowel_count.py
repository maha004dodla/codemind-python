s=input()
s=s.lower()
s=s.split(" ")
a=[]
for i in s:
    c=0
    for j in i:
        if j in "aeiou":
            c=c+1
    a.append(c)
b=max(a)
print(b)