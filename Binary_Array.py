n=int(input())
arr=list(map(int,input().split()))
b=0
for i in range(n):
    if(arr[i]==1 or arr[i]==0):
        b=b+1
if(b==n):
    print(True)
else:
    print(False)