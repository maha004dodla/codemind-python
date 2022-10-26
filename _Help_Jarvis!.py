n=int(input())
for i in range(n):
    a=int(input())
    m=a
    l=[]
    while(m!=0):
        r=m%10
        m=m//10
        l.append(r)
    l=sorted(l)
    length=len(l)
    c=0
    for i in range(length-1):
        if((l[i+1]-l[i])==1):
            c+=1
    if(c==(length-1)):
        print("YES")
    else:
        print("NO")
        
        