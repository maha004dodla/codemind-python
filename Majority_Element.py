n=int(input())
a=list(map(int,input().split()))
for i in a:
    if a.count(i)>(n//2):
        print(i)
        break