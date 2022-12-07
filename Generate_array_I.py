n=int(input())
arr=list(map(int,input().split()))
l=[]
m=[]
for i in range(n):
    if(i%2!=0):
        l.append(arr[i])
    if(i%2==0):
        m.append(arr[i])
n=[]
for i in range(len(m)):
    for j in range(0,l[i]):
        n.append(m[i])
print(*n)