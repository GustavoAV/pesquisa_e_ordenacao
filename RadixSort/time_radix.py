import timeit
import random

def radixSort(nums, base=10):
    array = []
    power = 0
    while nums:
        bins = [[] for _ in range(base)]
        for x in nums:
            bins[x // base**power % base].append(x)
        nums = []
        for bin in bins:
            for x in bin:
                if x < base**(power+1):
                    array.append(x)
                else:
                	nums.append(x)
        power += 1
    return array

array = list(range(60000))
random.shuffle(array)
#print(array)

sorted_array = radixSort(array)

tempo = timeit.timeit("radixSort({})".format(array), \
setup= "from __main__ import radixSort",number=1)

#print(sorted_array)
print(tempo)
