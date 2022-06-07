n=int(input())
for i in range(n):
    a=int(input())
    fact=1
    for i in range(2,a+1):
        fact=fact*i
    print(fact)