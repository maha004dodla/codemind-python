n=int(input())
arr=list(map(int,input().split()))
b=int(input())
l=[]
m=[]
for i in range(0,b):
    l.append(arr[i])
for j in range(b,n):
    m.append(arr[j])
for i in range(0,len(l)):
    for i in range(0,len(m)):
        print(l[i],m[i],end=" ")
    break

        