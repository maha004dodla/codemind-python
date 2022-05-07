s=input()
b=len(s)
ws=0
for i in range(0,b):
    ch=s[i]
    if(s[i]!=" "):
        ws=ws+1
print(ws)