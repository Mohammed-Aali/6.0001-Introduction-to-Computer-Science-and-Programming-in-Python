def fact_iter(n):
    prod = 1
    for i in range(1, n+ 1):
        prod *= i
    return prod

def fact_recur(n):
    """Assume n >= 0"""
    if n <= 1:
        return 1
    else:
        return n * fact_iter(n - 1)