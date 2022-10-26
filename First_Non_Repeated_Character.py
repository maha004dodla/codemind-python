n=int(input())
for i in range(n):
    a=int(input())
    s=input()
    s=list(s)
    flag=0
    for i in s:
        if(s.count(i)==1):
            print(i)
            flag=1
            break
    if(flag==0):
        print("-1")