def find_extreme_divisors(n1, n2):
    """Assumes that n1 and n2 are positive ints
       Returns a tuple containing the smallest common 
       divisor > 1 and the largest common divisor of n1 
       and n2"""
    min_value = None
    max_value = None
    for i in range(2, min(n1, n2), +1):
        if n1 % i == 0 and n2 % i == 0:
            if min_value == None or i < min_value:
                min_value = i
            if max_value == None or i > max_value:
                max_value = i

    return (min_value, max_value)

x = find_extreme_divisors(20, 100)
print(x)