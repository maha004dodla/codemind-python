n=int(input())
arr=list(map(int,input().split()))
x=int(input())
b=max(arr)
for i in range(n):
    c=arr[i]+x
    if(c>=b):
        print(True,end=" ")
    else:
        print(False,end=" ")