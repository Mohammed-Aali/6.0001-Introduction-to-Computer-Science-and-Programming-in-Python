def fib(n):
    """Assumes n in int >= 0
       return fibonacci of n"""
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
fib(5)