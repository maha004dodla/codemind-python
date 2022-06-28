n=int(input())
for i in range(2,(n//2)+1):
    if(n%i==0):
        print("Not Mega Prime")
        break
else:
    d=0
    c=0
    while(n>0):
        r=n%10
        n=n//10
        d=d+1
        if(r==2 or r==3 or r==5 or r==7):
            c=c+1
    if(d==c):
        print("Mega Prime")
    else:
        print("Not Mega Prime")