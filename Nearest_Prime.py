import math
def prime(p):
    if(p==1):
        return 1
    for i in range(2,int(math.sqrt(p)+1)):
        if(p%i==0):
            return 0
    else:
        return 1
n=int(input())
for i in range(n):
    a=int(input())
    for i in range(a,-1,-1):
        if(prime(i)):
            bf=i
            break
    aa=a+1
    while(1):
        if(prime(aa)):
            af=aa
            break
        aa+=1
    A=af-a
    B=a-bf
    if(A<B):
        print(af)
    elif(A==B):
        print(min(af,bf))
    else:
        print(bf)
            