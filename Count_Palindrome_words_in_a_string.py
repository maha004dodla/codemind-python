s=input()
s=s.lower()
S=s.split()
count=0
for i in S:
    a=i[::-1]
    if(i==a):
        count+=1
print(count)