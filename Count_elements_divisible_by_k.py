a,b=map(int,input().split())
arr=list(map(int,input().split()))
count=0
for i in range(a):
    if(arr[i]%b==0):
        count=count+1
print(count)