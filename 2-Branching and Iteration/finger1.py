iters_left = 10
odd = []

while(iters_left != 0):
    x = int(input('Enter a number: '))
    if x % 2 != 0:
        odd.append(x)
    iters_left -= 1

if odd:
    length = len(odd) - 1
    largest = 0
    while(length != -1):
        if odd[length] > largest:
           largest = odd[length]
        length -= 1
       
    print(largest)
else:
    print('no odd numbers')