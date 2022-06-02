s=input()
c=0
for i in s:
    if i in "aeiouAEIOU":
        c=c+1
    if(i==" "):
        print(c,end=" ")
        c=0
print(c)