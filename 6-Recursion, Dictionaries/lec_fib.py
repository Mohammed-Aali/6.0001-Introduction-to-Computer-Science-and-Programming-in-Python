def fib(x):
    """Assume x is an int >= 0
       returns fibonacci of x"""
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)
    
print(fib(9))