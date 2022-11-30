n=int(input())
flag=0
for i in range(-31,31):
    if(2**i==n):
        flag=1
if(flag==1):
    print("True")
else:
    print("False")