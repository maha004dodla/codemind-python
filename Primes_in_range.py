def prime(n):
    if(n==1):
        return 0
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return 0
    return 1
n1=int(input())
n2=int(input())
sum,count=0,0
for i in range(n1,n2+1):
    if(prime(i)):
        sum=sum+i
        count=count+1
print(count)