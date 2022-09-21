n=int(input())
for i in range(n):
    a=int(input())
    a=str(a)
    b=int(a,2)
    c=oct(b)
    d=c.replace("0o","")
    print(d)