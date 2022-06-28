n=int(input())
arr=list(map(int,input().split()))
flag=0
for i in range(n):
    if(arr[i]%2==0 and i%2!=0):
        flag=1
if(flag==1):
    print("False")
else:
    print("True")