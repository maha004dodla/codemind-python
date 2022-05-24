n=int(input())
arr=list(map(int,input().split()))
b=[]
for i in range(len(arr)):
    a=arr[i]**2
    b.append(a)  #[16 1 0 9 100]
b.sort()
print(*b)