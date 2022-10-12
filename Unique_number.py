N=int(input())
n=N
l=[]
m=[]
while(n!=0):
    r=n%10
    l.append(r)
    n=n//10
for i in l:
    a=l.count(i)
    m.append(a)
c=0
for i in m:
    if(i==1):
        c+=1
if(c==len(str(N))):
    print("Unique Number")
else:
    print("Not Unique Number")