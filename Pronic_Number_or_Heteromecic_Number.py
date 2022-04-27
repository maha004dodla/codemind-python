a=int(input())
flag=0
for i in range(a):
    if(i*(i+1)==a):
        flag=1
if(flag==1):
    print('YES')
else:
    print('NO')