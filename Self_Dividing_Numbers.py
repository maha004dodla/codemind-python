a=int(input())
b=int(input())
for i in range(a,b+1):
    if(len(str(i))==1):
        print(i,end=" ")
    elif('0' not in str(i)):
        m=i
        count=0
        while(m!=0):
            r=m%10
            m=m//10
            if(i%r==0):
                count+=1
        if(count==len(str(i))):
            print(i,end=" ")
    