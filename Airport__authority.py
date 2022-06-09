n=int(input())
b=[]
for i in range(0,n):
    a=int(input())
    b.append(a)
t=int(input())
x=0
for i in range(len(b)):
    if(b[i]<=t):
        x=x+1
    else:
        x=x+2
print(x)