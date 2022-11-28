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
while(i<len(e) or j<len(o)):
    if(i<len(e)):
        l.append(e[i])
    i+=1
    if(j<len(o)):
        l.append(o[j])
    j+=1
if(len(l)%2!=0):
    l.append(0)
print(*l)