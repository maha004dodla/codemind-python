n=int(input())
arr=list(map(int,input().split()))
e=[]
o=[]
for i in range(0,n):
    if(arr[i]%2==0):
        e.append(arr[i])
    if(arr[i]%2!=0):
        o.append(arr[i])
i,j=0,0
l=[]
while(i<len(o) or j<len(e)):
    if(i<len(o)):
        l.append(o[i])
    i+=1
    if(j<len(e)):
        l.append(e[j])
    j+=1
if(len(l)%2!=0):
    l.append(0)
print(*l)