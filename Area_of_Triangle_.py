a,b,c=map(int,input().split())
s=(a+b+c)/2
ss=s*(s-a)*(s-b)*(s-c)
import math
area=math.sqrt(ss)
print('%0.2f'%area)