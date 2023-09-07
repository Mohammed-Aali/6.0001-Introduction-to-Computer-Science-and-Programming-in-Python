def bisection_search(L, e):
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        half = len(L) / 2
        if half > e:
            return bisection_search(L[:half], e)
        else:
            return bisection_search(L[half:], e)

#implementation 2
def bisection_search(L, e):
    def bisection_mod(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high) / 2
        
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:
                return False
            else:
                return bisection_mod(L, e, low, mid - 1)
        else:
            return bisection_mod(L, e, mid + 1, high)
    
    if len(L) == 0:
        return False
    else:
        return bisection_mod(L, e, 0, len(L))
