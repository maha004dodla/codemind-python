n=int(input())
arr=list(map(int,input().split()))
l=[]
for i in arr:
    a=len(str(i))
    l.append(a)
b=max(l)
count=0
for i in l:
    if(i==b):
        count=count+1
print(count)