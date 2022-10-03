s=input()
s1=""
for i in s:
    if i not in s1:
        s1=s1+i
if(s1==s):
    print("True")
else:
    print("False")