A=list(map(int,input().split()))
B=list(map(int,input().split()))
a=0
b=0
if(A[0]>B[0]):
    a=a+1
elif(A[0]<B[0]):
    b=b+1
if(A[1]>B[1]):
    a=a+1
elif(A[1]<B[1]):
    b=b+1
if(A[2]>B[2]):
    a=a+1
elif(A[2]<B[2]):
    b=b+1
print(a,b)