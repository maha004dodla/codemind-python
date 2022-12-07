n=int(input())
arr=list(map(int,input().split()))
i,j=0,n-1
l=[]
while(i<=j):
    if(i==j):
        l.append(arr[i])
        break
    l.append(arr[i])
    l.append(arr[j])
    i+=1
    j-=1
if(len(l)%2!=0):
    l.append(0)
    print(*l)
else:
    print(*l)
    