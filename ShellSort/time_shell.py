import timeit
import random

def shellSort(array): 
    
    n = len(array) 
    gap = n/2

    while gap > 0: 
        for i in range(gap,n): 
            temp = array[i] 
            j = i 
            while  j >= gap and array[j-gap] >temp: 
                array[j] = array[j-gap] 
                j -= gap 
            array[j] = temp 
        gap /= 2

array = list(range(70000))
random.shuffle(array)
#print(array)

shellSort(array)

tempo = timeit.timeit("shellSort({})".format(array), \
setup= "from __main__ import shellSort",number=1)

#print(array)
print(tempo)
