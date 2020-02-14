import timeit
import random

def insertionSort(array):
   for index in range(1,len(array)):

     currentvalue = array[index]
     position = index

     while position>0 and array[position-1]>currentvalue:
         array[position]=array[position-1]
         position = position-1

     array[position]=currentvalue

array = list(range(60000))
random.shuffle(array)

insertionSort(array)

tempo = timeit.timeit("insertionSort({})".format(array), \
setup= "from __main__ import insertionSort",number=1)

print(array)
print(tempo)
