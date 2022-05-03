n=int(input())
flag=0
for i in range(n+1):
    if(n==i*i):
        flag=1
        break
if(flag==1):
    print('True')
else:
    print('False')
    