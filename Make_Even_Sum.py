n=int(input())
arr=list(map(int,input().split()))
sum=0
for i in arr:
    sum=sum+i
if(sum%2==0):
    print("1")
else:
    print("0")