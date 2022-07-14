s=input()
l=s.split()
for i in l:
    a=ord(min(i))
    b=ord(max(i))
    print(abs(a-b),end=" ")