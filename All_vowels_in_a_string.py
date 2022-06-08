s=input()
l=0
u=0
a=[]
b=[]
for i in s:
    if i in "aeiou":
        if i not in a:
            a.append(i)
            l=l+1
    if i in "AEIOU":
        if i not in b:
            b.append(i)
            u=u+1
if(l==5 or u==5):
    print(True)
else:
    print(False)