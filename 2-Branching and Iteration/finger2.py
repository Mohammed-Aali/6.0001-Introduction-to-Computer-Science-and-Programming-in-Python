s = '1.23,2.4,3.123'
sum = 0
for n in s:
    if n.isdigit():
        sum = sum + int(n)

print(sum)
