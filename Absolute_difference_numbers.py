a,b=map(int,input().split())
c=str(a)
d=c[::-1]
C=c[:b]
D=d[:b]
D=D[::-1]
E=int(C)-int(D)
print(abs(E))