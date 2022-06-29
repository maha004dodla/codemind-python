n=int(input())
arr=list(map(int,input().split()))
b=sum(arr)
c=b//n
flag=0
for i in arr:
    if c in arr:
        flag=1
if(flag==0):
    print(False)
else:
    print(True)