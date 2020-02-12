import timeit
import random

def selectionSort(array):
    for index in range(0, len(array)):
        min_index = index

        for right in range(index + 1, len(array)):
            if array[right] < array[min_index]:
                min_index = right

        array[index], array[min_index] = array[min_index], array[index]

array = list(range(60000))
#random.shuffle(array)

selectionSort(array[::-1])
#selectionSort(array)

tempo = timeit.timeit("selectionSort({})".format(array), \
setup= "from __main__ import selectionSort",number=1)

print(array)
print(tempo)
