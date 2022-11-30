n=int(input())
arr=list(map(int,input().split()))
for i in arr:
    a=arr.count(i)
    if(a==1):
        print(i)