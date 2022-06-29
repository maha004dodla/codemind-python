r,c=map(int,input().split())
s=[]
for i in range(0,r):
    l=list(map(int,input().split()))
    s.append(l)
sum,sum1=0,0
for i in range(0,r):
    for j in range(0,c):
        if(s[i][j]%2==0):
            sum=sum+s[i][j]
        if(s[i][j]%2!=0):
            sum1=sum1+s[i][j]
print(sum,sum1)