s=input()
s=s.lower()
s=s.replace(" ","")
s=list(s)
l=""
for i in s:
    a=s.count(i)
    if(a==1):
        l+=i
b=sorted(l)
c="".join(b)
print(c)
