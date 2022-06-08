n = list(map(str,input().split()))
for i in range(0,len(n)):
    for j in range(0,len(n)):
        if(i!=j and n[i]<n[j]):
            n[i],n[j]=n[j],n[i]
print(*n)