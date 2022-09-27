n=int(input())
arr=list(map(int,input().split()))
a=sorted(arr)
l=[]
for i in a:
    b=len(str(i))
    l.append(b)
c=max(l)
for i in a:
    if(len(str(i))==c):
        print(i,end=" ")