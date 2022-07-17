n=int(input())
for i in range(n):
    a=int(input())
    arr=list(map(int,input().split()))
    f=0
    for i in range(a):
        ls=sum(arr[:i])
        rs=sum(arr[i+1:])
        if ls==rs:
            f=1
            break
    if(f==1):
        print("YES")
    else:
        print("NO")