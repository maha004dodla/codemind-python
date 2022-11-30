n=int(input())
a=str(abs(n))
b=a[::-1]
if(n<0):
    print((-1)*int(b))
else:
    print(int(b))