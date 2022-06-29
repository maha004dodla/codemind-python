r,c=map(int,input().split())
s=[]
for i in range(0,r):
    l=list(map(int,input().split()))
    s.append(l)
sum=0
for i in range(0,r):
    for j in range(0,c):
        sum=sum+s[i][j]
print(sum)