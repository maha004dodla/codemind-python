n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    flag=0
    for i in range(0,b):
        if((i*i)%b==a):
            print(i)
            flag=1
            break
    if(flag==0):
        print("-1")