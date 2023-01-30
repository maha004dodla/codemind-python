def pal(p):
    a=str(p)
    b=a[::-1]
    return int(b)
n=int(input())
while(n):
    n+=int(pal(n))
    if(n==pal(n)):
        print(n)
        break