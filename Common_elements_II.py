n , m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
for i in a:
    if i not in b:
        print(i,end=" ")
for i in b:
    if i not in a:
        print(i,end=" ")