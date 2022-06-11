s=input()
n = s.lower()
n = n.replace(" ","")
count = 0
for i in range(0,len(n)):
    c = n.count(n[i])
    if c==1:
        count+=1
if count==0:
    print("-1")
else:
    print(count)