n=int(input())
arr=list(map(int,input().split()))
arr=sorted(arr)
b=list(set(arr))
mini,c=0,0
for i in range(n):
    c=0
    for j in range(1,n):
        if(arr[i]==arr[j]):
            c+=1
        if(mini<c):
            mini=c
if(len(b)==1):
    print("0")
else:
    print(mini)
