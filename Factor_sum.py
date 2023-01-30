n=input()
n=n.replace(",","")
n=list(n)
l=[]
for i in n:
    l.append(int(i))
sum=0
m=[]
for i in l:
    a=i
    sum=0
    for i in range(1,a+1):
        if(a%i==0):
            sum+=i
    m.append(sum)
n=[]
flag=0
for i in range(len(l)):
    for j in range(len(m)):
        if m[i] in l:
            n.append(l[i])
            break
n=sorted(n)
if(len(n)==0):
    print("-1")
else:
    print(*n)
    
    