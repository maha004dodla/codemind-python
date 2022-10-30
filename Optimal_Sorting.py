n=int(input())
for i in range(n):
    a=int(input())
    b=list(map(int,input().split()))
    c=sorted(b)
    if(b==c):
        print("0")
    else:
        print(c[-1]-c[0])
    