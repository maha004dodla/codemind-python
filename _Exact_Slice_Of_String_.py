s=input()
a=int(input())
b=int(input())
for i in range(len(s)):
    if(i>=a and i<=b):
        print(s[i],end="")