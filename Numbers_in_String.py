a=input()
sum1 = 0
for i in a:
    if ord(i) >= 48 and ord(i) <= 57:
        sum1 = sum1 + int(i)
print(str(sum1))