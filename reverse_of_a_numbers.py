a=int(input())
sum=0
while(a!=0):
    r=a%10
    a=a//10
    sum=(sum*10)+r
print(sum)