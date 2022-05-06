n=int(input())
sum=0
while(n>0 or sum>9):
    if(n==0):
        n=sum
        sum=0
    r=n%10
    sum=sum+r
    n=n//10
print(sum)