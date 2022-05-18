n=int(input())
x=n
sum=0
while(x>0):
    r=x%10
    x=x//10
    fact=1
    for i in range(1,r+1):
        fact=fact*i
    sum=sum+fact
if(sum==n):
    print("The number",n,"is a strong number")
else:
    print("The number",n,"is not a strong number")