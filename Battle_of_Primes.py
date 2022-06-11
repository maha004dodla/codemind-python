def prime(n):
    while n:
        c = 0
        for i in range(2,n//2):
            if n%i==0:
                c+=1
        if c==0:
            return n
        n+=1
        
a = int(input())
b = int(input())
print(prime(a+b+1)-(a+b))