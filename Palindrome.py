n=int(input())
a=n
sum=0
while(n>0):
    r=n%10
    sum=r+(sum*10)
    n=n//10
if(a==sum):
  print("True")
else:
  print("False")