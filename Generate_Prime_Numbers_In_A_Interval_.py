def Prime(n):
    for i in range(2,(n//2)+1):
        if(n%i==0):
            return 0
    return 1
n1=int(input())
n2=int(input())
for i in range(n1+1,n2+1):
    if(Prime(i)):
        print(i,end="
")