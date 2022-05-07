s=input()
b=len(s)
d=0
c=0
v=0
ws=0
for i in range(0,b):
    ch=s[i]
    if(s[i]>='0' and s[i]<='9'):
        d=d+1
    elif(s[i]==' '):
        ws=ws+1
    elif(s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u' or s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U'):
        v=v+1
    else:
        c=c+1
print('Vowels:',v)
print('Consonants:',c)
print('Digits:',d)
print('White spaces:',ws)
        