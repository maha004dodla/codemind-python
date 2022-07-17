n=int(input())
s=[]
a=0
b=0
for i in range(n):
    l=list(map(int,input().split()))
    s.append(l)
for i in range(n):
    for j in range(n):
        if(i==j):
            a=a+s[i][j]
        if(i+j==n-1):
            b=b+s[i][j]
print('Principal Diagonal:',end='')
print(a)
print('Secondary Diagonal:',end='')
print(b)