import timeit
import random

def countingSort(array):
     highest = max(array) + 1
     helper_list = [0] * highest
     s_list = []
     for value in array:
         helper_list[value] += 1

     for j in range(len(helper_list)):
         s_list.extend([j] * helper_list[j])

     return s_list

array = list(range(100))
random.shuffle(array)
#print(array)

sorted_array = countingSort(array)

tempo = timeit.timeit("countingSort({})".format(array), \
setup= "from __main__ import countingSort",number=1)

#print(sorted_array)
print(tempo)
