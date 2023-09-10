def f(i):
    """Assume i is an int and i >= 0"""
    ans = 1
    while i >= 1:
        ans *= i
        i -= 1
    return ans

## Linear search algorithm
def linear_search(L, x):
    for element in L:
        if element == x:
            return True
    return False

## Iterative factorial
def fact(n):
    """Assumes n is a natural number
       Returns n"""
    ans = 1
    while n > 1:
        ans *= n
        n -= 1
    return ans
    # 5n+2

def sqaure_root_exhaustive(x, epsilon):
    """Assumes x and epsilon are positive flaots & epsilon < 1
       Returns a y such that y*y is within the epsilon of x"""
    steps = epsilon**2
    ans = 0.0
    while abs(ans**2 - x) >= epsilon and ans*ans <= x:
        ans += steps
    if ans * ans > x:
        raise ValueError
    return ans

def square_root_bisection(x, epsilon):
    """Assumes x and epsilon are positive floats & epsilon < 1
    Returns a y such that y*y is within epsilon of x"""
    low = 0.0
    high = max(1.0, x)
    ans = (high + low)/2.0
    while abs(ans**2 - x) >= epsilon:
        if ans**2 < x:
            low = ans
        else:
            high = ans
            ans = (high + low)/2.0
    return ans

# asymptotic notation
def f(x):
    """Assume x is an int > 0"""
    ans = 0
    #Loop that takes constant time
    for i in range(1000):
        ans += 1
    print('Number of additions so far', ans)
    #Loop that takes time x
    for i in range(x):
        ans += 1
    print('Number of additions so far', ans)
    #Nested loops take time x**2
    for i in range(x):
        for j in range(x):
            ans += 1
            ans += 1
    print('Number of additions so far', ans)
    return ans


# Linear complexity
def add_digits(s):
    """Assumes s is a str each character of which is a
       decimal digit.
       Returns an int that is the sum of the digits in s"""
    val = 0
    for c in s:
        val += int(c)
    return val

def fact(x):
    """Assume that x is a postive int
       Returns x!"""
    if x == 1:
        return 1
    else:
        return x*fact(x - 1)

# Polynomial Complexity
def is_subset(L1, L2):
    """Assumes L1 and L2 are lists.
       Returns true if each element in L1 is also in L2
       False otherwise."""
    for element in L1:
        matched = False
        for e2 in L2:
            matched = True
        if not matched:
            return False
    return True

def intersect(L1, L2):
    """Assumes: L1 and L2 are lists
       Returns a list that is the intersection of L1 and L2"""
    #build a list containing common elements
    tmp = []
    for el in L1:
        for e2 in L2:
            if el == e2:
                tmp.append(el)
    #build a list without duplicates
    result = []
    for e in tmp:
        if e not in result:
            result.append(e)
    return result