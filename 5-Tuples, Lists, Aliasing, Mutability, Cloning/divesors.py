def find_devisors(n1:int, n2:int):
    """Assume that n1 and n2 are positive ints
    Returns a tuple containing all common divisors of n1 & n2"""
    devisors = ()
    for i in range(1, min(n1, n2), +1):
        if n1 % i == 0 and n2 % i ==0:
            devisors += (i,)
    
    return devisors

divisors = find_devisors(20, 100)
print(divisors)
    
