n=int(input())
for i in range(n):
    a=input()
    b=int(a,8)
    c=bin(b)
    d=c.replace("0b","")
    print(d)