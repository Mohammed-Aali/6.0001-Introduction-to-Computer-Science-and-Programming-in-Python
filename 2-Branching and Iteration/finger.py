x = 20
y = 40
z = 4
li = [x, y, z]
li1 = []


for element in li:
    if element % 2 != 0:
        li1.append(element)

largest = 0
for element in li1:
    if element > largest:
        largest = element
        
if li1:
    print(largest)
else:
    print('no odd numbers')
