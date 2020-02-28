import timeit
import random

def mergeSort(array):
    if len(array) < 20:
        return sorted(array)
    result = []
    mid = int(len(array) / 2)
    y = mergeSort(array[:mid])
    z = mergeSort(array[mid:])
    i = 0
    j = 0
    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1
    result += y[i:]
    result += z[j:]
    return result

array = list(range(100))
random.shuffle(array)

sorted_array = mergeSort(array)

tempo = timeit.timeit("mergeSort({})".format(array), \
setup= "from __main__ import mergeSort",number=1)

print(sorted_array)
print(tempo)
