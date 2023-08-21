def apply_to_each(L, f):
    """Assumes L is a list, f a function
       Mutatest L by replacing each elemnet e of L by f(e)"""
    for i in range(len(L)):
        L[i] = f(L[i])

L = [1, -2, 3.33]
print('L =', L)
print('Apply absulote value to each element of L.')
apply_to_each(L, abs)
print('L =', L)
print('Apply int to each element in L')
apply_to_each(L, int)
print('L =', L)