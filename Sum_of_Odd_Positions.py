n=int(input())
arr=list(map(int,input().split()))
es=0
os=0
for i in range(n):
    if(i%2!=0):
        os=os+arr[i]
import math
print(abs(os))