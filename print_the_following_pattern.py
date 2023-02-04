n=int(input())
for i in range(0,n):
    for j in range(n-i,0,-1):
        print(chr(65+(n-i-1)),end=" ")
    print()