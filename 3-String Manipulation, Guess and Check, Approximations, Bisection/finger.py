number = int(input('Enter an integer: '))

# starts at 1 because I won't count 0
pwr = 1

# indicates if we found the final powers and such
found = False

while pwr < 6:
    root = 0
    while root < number:
        x = root**pwr
        if x == number:
            found = True
            break
        else:
            found = False
        root+=1

    if found:
        break
    
    pwr+=1
    
if found:
    print('the root of', number, 'is', root)
    print('the power of', root, 'is', pwr)
else:
    print('could not find a number')