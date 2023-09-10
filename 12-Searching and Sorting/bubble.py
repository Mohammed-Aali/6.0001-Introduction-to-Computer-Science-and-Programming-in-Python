def bubble_sort(L):
    swap = False
    while not swap:
        print('Bubble sort: ' + str(L))
        swap = True
        for j in range(1, len(L)):
            if L[j- 1] > L[j]:
                swap = False
                tmp = L[j]
                L[j] = L[j - 1]
                L[j - 1] = tmp

# O(n^2)
test_list = [1, 3, 5, 7, 2, 6, 25, 18, 13, 8]

print("")
print(bubble_sort(test_list))
print(test_list)

# selection sort
def selection_sort(L):
    suffix_st = 0
    while suffix_st != len(L):
        for i in range(suffix_st, len(L)):
            if L[i] < L[suffix_st]:
                L[suffix_st], L[i] = L[i], L[suffix_st]
        suffix_st += 1

# O(n^2)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def merge_sort(L):
    print('merge soert: ' + str(L))
    if len(L) < 2:
        return L[:]
    else:
        mid = len(L) // 2
        left = merge_sort(L[:mid])
        right = merge_sort(L[mid:])
        return merge(left, right)

print("")
print(merge_sort(test_list))