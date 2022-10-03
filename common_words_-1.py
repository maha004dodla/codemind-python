s=input()
s1=input()
s=s.lower()
s1=s1.lower()
s=s.split(" ")
s1=s1.split(" ")
c=0
for i in s:
    if i in s1:
        c=c+1
print(c)
