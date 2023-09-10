def search(L, e):
    """Assumes L is a list, the elements of which are in
    ascending order.
    Returns True if e is in L and False otherwise"""
    def bSearch(L, e, low, high):
        #Decrements high - low
        if high == low:
            return L[low] == e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid: #nothing left to search
                return False
            else:
                return bSearch(L, e, low, mid - 1)
        else:
            return bSearch(L, e, mid + 1, high)
    if len(L) == 0:
        return False
    else:
        return bSearch(L, e, 0, len(L) - 1)
    
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 20]
print(search(l, 19))