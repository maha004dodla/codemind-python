s=input()
s=s.replace(" ","")
s=s.lower()
s1=""
for i in s:
    a=s.count(i)
    if(a==1):
        s1+=i
b=sorted(s1)
c="".join(b)
print(c)