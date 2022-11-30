n=int(input())
for i in range(2**n):
    a=bin(i)
    b=a.replace("0b","")
    c=len(b)
    if(c==n):
        print(b)
    else:
        A=""
        d=n-c
        for i in range(d):
            A+="0"
        print(A+b)
        