n=int(input())
for i in range(n):
    a=input()
    b=int(a,16)
    c=bin(b)
    d=c.replace("0b","")
    e=len(d)
    if(e%4!=0):
       f=4-(len(d)%4)
       A=""
       for i in range(f):
           A+='0'
       print(A+d)
    else:
        print(d)
           