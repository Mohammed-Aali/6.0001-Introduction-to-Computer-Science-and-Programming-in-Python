L = [x**2 for x in range(1,7) if x % 2 == 0]

mixed = [1, 2, 3, 'a', 4.0]
print([x**2 for x in mixed if type(x) == int])