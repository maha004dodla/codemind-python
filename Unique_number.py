n=int(input())
l=[0,0,0,0,0,0,0,0,0,0]
while n:
    r=n%10
    l[r]=l[r]+1
    n=n//10
for i in l:
    if i>1:
        print("Not Unique Number")
        break
else:
    print("Unique Number")