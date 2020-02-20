from timeit import timeit
from random import random

randomList = [random() for num in range(500_000)]

def qsort(values):
    if len(values) < 2: return values
    return qsort([val for val in values if val < values[0]]) +  \
    [values[0]] + \
    qsort([val for val in values if val > values[0]])

time1 = timeit('qsort(randomList)', globals=globals(), number=100)
print('super-simple qsort: ' + str(time1))
