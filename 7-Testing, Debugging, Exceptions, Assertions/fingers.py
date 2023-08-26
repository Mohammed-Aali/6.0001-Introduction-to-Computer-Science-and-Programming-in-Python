def findAnEven(l):
    """Assumes l is a list of integers
    Returns the first even number in l
    Raises ValueError if l does not contain an even number"""
    for i in l:
        if i % 2 == 0:
            return i
        
    raise ValueError('findAnEven was called with no even number')

print(findAnEven([3,5,65, 9]))