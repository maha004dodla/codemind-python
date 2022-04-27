n=int(input())
a=0
b=1
print('0 1 ',end='')
for i in range(2,n):
    c=a+b
    print(c,end=' ')
    a=b
    b=c