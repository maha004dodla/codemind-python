s=input()
c=0
a=[]
for i in s:
    if i in "aeiouAEIOU":
        if i not in a:
            a.append(i)
        c=c+1
if(c==0):
    print("-1")
else:
    print(*a)