# iterative factorial
def factI(n):
    """Assume theat n is an inte > 0
       Returns n!"""
    result = 1
    while n > 1:
        result = result * n
        n -= 1
    return result

def factR(n):
    """Assume that n is an int > 0
       Returns n!"""
    if n == 1:
        return n
    else:
        return n*factR(n - 1)
    
print(factR(3))