n=int(input())
arr=list(map(int,input().split()))
count=0
for i in arr:
    a=str(i)
    b=a[::-1]
    c=int(b)
    if(i==c):
        count+=1
print(count)