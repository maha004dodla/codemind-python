a=input().lower()
b=input().lower()
a=a.split()
b=b.split()
c=0
for i in a:
    if i in b :
        if(b.count(i)==a.count(i)):
            c+=1
print(c)

