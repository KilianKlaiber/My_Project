from random import shuffle
from functions import parallel_process

def number_of_processes(func):
    process_number =  0
    def wrapper( *args, **kwargs):
        nonlocal process_number
        process_number += 1
        print(process_number)
        result = func( *args, **kwargs)
        #process_number += -1
        return result
    return wrapper

""" 
@number_of_processes
def summation(a,b):
    return a + b

summation(5, 10)"""

arrangement = list(range(50))

shuffle(arrangement)

@number_of_processes
def quick_parallel_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        
        result = parallel_process(quick_parallel_sort, [left, right])
        
        return result[0] + middle + result[1]

print(arrangement)

quick_parallel_sort(arrangement)


