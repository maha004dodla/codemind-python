s=input()
s=s.split()
for i in range(len(s)):
    for j in range(len(s)):
        if((len(s[i])<len(s[j]))):
            s[i],s[j]=s[j],s[i]
print(*s)
