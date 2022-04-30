n=int(input())
arr=list(map(int,input().split()))
sum=0
s=0
for i in range(len(arr)):
   if(arr[i]%2==0):
       print(arr[i],end=" ")
for i in range(len(arr)):
   if(arr[i]%2!=0):
       print(arr[i],end=" ")