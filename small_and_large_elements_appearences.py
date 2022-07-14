s=input()
s1=s.split()
a=max(s)
b=max(s)
for i in s1:
    for j in i:
        if(j<b):
            b=j
print(b,s.count(b),a,s.count(a))