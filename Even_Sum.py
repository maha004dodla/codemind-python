n=int(input())
arr=list(map(int,input().split()))
es=0
os=0
for i in range(n):
    if(arr[i]%2==0):
        es=es+arr[i]
import math
print(abs(es))