a,b=map(int,input().split())
from itertools import permutations
s=""
l=[]
for i in range(1,a+1):
    s+=str(i)
for i in permutations(s):
    c="".join(i)
    l.append(int(c))
for i in range(1,len(l)+1):
    if(i==b):
        print(l[i-1])