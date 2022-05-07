s=input()
b=len(s)
d=0
for i in range(0,b):
    ch=s[i]
    if(s[i]>='0' and s[i]<='9'):
        d=d+1
if(d>0):
    print('Contains',d,'digit')
else:
    print("Doesn't contain digit")