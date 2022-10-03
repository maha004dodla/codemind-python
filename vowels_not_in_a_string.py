s=input()
s=s.lower()
s1=""
flag=0
for i in "aeiou":
   if i not in s:
       s1+=i
       print(i,end=" ")
       flag=1
if(flag==0):
    print("0")

        