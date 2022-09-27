n=int(input())
arr=list(map(int,input().split()))
a=sorted(arr)
l=[]
for i in a:
    b=len(str(i))
    l.append(b)
d=0
for i in l:
    c=min(l)
    if(i==c):
        d=d+1
print(d)