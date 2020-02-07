import timeit

def bubbleSort(arr):
    n = len(arr)
 
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = list(range(60000))

bubbleSort(arr[::-1])

tempo = timeit.timeit("bubbleSort({})".format(arr), \
setup= "from __main__ import bubbleSort",number=1)

print(tempo)
