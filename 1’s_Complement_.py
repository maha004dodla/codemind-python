a=int(input())
b=bin(a)
c=b.replace("0b","")
d=list(c)
l=[]
for i in d:
    if(i=="0"):
        l.append("1")
    if(i=="1"):
        l.append("0")
e="".join(l)
print(int(e,2))