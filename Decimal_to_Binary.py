n=int(input())
for i in range(n):
    a=int(input())
    b=bin(a)
    c=b.replace("0b","")
    print(c)