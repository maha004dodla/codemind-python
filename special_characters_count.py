s=input()
c=0
for i in s:
    if i not in "0123456789":
        if i not in "abcdefghijklmnopqrstuvwxyz":
            if i not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                if i not in " ":
                    c=c+1
print(c)