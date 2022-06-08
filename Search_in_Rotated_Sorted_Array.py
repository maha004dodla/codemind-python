n=int(input())
arr=list(map(int,input().split()))
x=int(input())
c=0
for i in range(n):
    if(x==arr[i]):
        print(i)
        c=c+1
if(c==0):
    print("-1")