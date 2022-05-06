n=int(input())
sum=0
while(sum!=1 and sum!=4):
    sum=0
    while(n!=0):
        r=n%10
        sum=sum+(r*r)
        n=n//10
    n=sum
if(sum==1):
    print(True)
else:
    print(False)