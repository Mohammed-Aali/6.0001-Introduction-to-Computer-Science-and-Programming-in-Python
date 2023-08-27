try:
    a = int(input('Tell me one number: '))
    b = int(input('Tell me another number: '))
    print('a/b =', a/b)
except ValueError:
    print('Could not convert to a number.')
except ZeroDivisionError:
    print('Cannot divide by zero.')
except:
    print('Something went very wrong.')