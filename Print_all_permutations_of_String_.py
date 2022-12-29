from itertools import permutations
s=input()
l=[]
for i in permutations(s):
    a="".join(i)
    l.append(a)
for i in l:
    print(i)