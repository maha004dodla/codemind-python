def prime(n):
    for i in range(2,(n//2)+1):
        if(n%i==0):
            return(False)
    else:
        return(True)
def rev(n):
    rev=0
    while(n):
        r=n%10
        n=n//10
        rev=(rev*10)+r
    return rev
n=int(input())
if(prime(n)):
    if prime(rev(n)):
       print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")