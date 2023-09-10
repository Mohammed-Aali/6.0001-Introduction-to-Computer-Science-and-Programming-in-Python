def intToStr(i):
    """Assumes i is a nonnegative int
    Returns a decimal string representation of i"""
    digits = '0123456789'
    if i == 0:
        return '0'
    result = ''
    while i > 0:
        result = digits[i%10] + result
        i = i//10
    return result

x = intToStr(65688)
print(x)

def add_digits(s):
    """Assumes n is a nonnegative int
    Returns the sum of the digits in n"""
    stringRep = intToStr(s)
    val = 0
    for c in stringRep:
        val += int(c)
    return val