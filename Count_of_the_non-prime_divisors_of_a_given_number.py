n=int(input())
sum=0
for i in range(1,n+1):
    if(n%i==0):
        if i>=1:
            count=0
            for j in range(2,i):
                if(i%j==0):
                    count=count+1
            if(count!=0):
                sum=sum+1
print(sum+1)