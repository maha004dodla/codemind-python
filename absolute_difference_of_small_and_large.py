s=input()
m=s.split(" ")
for i in range(0,len(m)):
    mini=ord(min(m[i]))
    maxi=ord(max(m[i]))
    print(abs(mini-maxi),end=" ")