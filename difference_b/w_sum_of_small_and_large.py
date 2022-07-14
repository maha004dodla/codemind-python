s=input()
l=s.split()
a,b=0,0
for i in l:
    a=a+ord(min(i))
    b=b+ord(max(i))
print(b-a)