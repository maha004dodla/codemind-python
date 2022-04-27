a,b=map(int,input().split())
i=1
while(a*i%b!=0):
    i=i+1
print(a*i)