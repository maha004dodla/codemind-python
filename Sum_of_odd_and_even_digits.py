n=int(input())
arr=list(map(int,input().split()))
sum=0
s=0
for i in range(len(arr)):
   if(i%2==0):
       sum=sum+arr[i]
   elif(i%2!=0):
       s=s+arr[i]
d=sum-s
if(d==0):
    print("YES")
else:
    print("NO")