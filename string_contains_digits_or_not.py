n=int(input())
for i in range(n):
    s=input()
    flag=0
    for i in s:
        if i in "0123456789":
            flag=1
            break
    if(flag==1):
        print("Yes")
    else:
        print("No")