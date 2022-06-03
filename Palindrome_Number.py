n=int(input())
i=1
for i in range(n):
    a=int(input())
    sum=0
    temp=a
    while(temp>0):
       r=temp%10
       sum=(sum*10)+r
       temp=temp//10
    if(sum==a):
        print("True")
    else:
        print("False")