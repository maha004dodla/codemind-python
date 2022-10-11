n=int(input())
for i in range(n):
    s=input()
    a=s[::-1]
    if(s==a and len(s)%2==0):
        print("YES EVEN")
    elif(s==a and len(s)%2!=0):
        print("YES ODD")
    else:
        print("NO")