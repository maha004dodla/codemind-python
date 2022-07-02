n=int(input())
arr=list(map(int,input().split()))
sum,count=0,0
for i in range(n):
    c=0
    for j in range(n):
        if(arr[i]==arr[j]):
            c=c+1
    if(c==arr[i]):
        sum=sum+arr[i]
        count=count+1
        arr[i]=0
if(sum==0):
    print("-1")
else:
    avg=float(sum)/count
    print("%0.2f"%avg)