n=int(input())
arr=list(map(int,input().split()))
e=[]
o=[]
for i in range(n):
    if(arr[i]%2==0):
        e.append(arr[i])
    if(arr[i]%2!=0):
        o.append(arr[i])
i,j=0,0
while(i<len(e) or j<len(o)):
    if(i<len(e)):
        print(e[i],end=" ")
        i=i+1
    if(j<len(o)):
        print(o[j],end=" ")
        j=j+1
if(n%2!=0):
    print("0")