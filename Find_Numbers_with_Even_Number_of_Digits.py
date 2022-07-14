def digits(n):
    d=0
    while n:
        n=n//10
        d+=1
    return d
n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if(digits(i)%2==0):
        c+=1
print(c)