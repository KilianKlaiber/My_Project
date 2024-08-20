# Count number of threads, which are running simultaneously 

from random import shuffle
from functions import parallel_process

def number_of_processes(func):
    process_number =  0
    def wrapper(*args, **kwargs):
        nonlocal process_number
        process_number += 1
        print(process_number)
        result = func(*args, **kwargs)
        process_number += -1
        return result
    return wrapper


@number_of_processes
def summation(a,b):
    return a + b

for _ in range(10):
    summation(5, 10)

arrangement = list(range(50))

shuffle(arrangement)


# @number_of_processes
def quick_parallel_sort(arr: list) -> list | None:
    """sort unsorted list of items
    by pivoting the list item recusively around a pivot.
    Recursive processing of left and right sublists is performed in parallel.

    Args:
        arr (list): list of unsorted items

    Returns:
        list | None: list of sorted items, None if program crashes.
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        result = parallel_process(quick_parallel_sort, [left, right])
        
        if result == None:
            print("quick_parallel_sort crashed")
            return None
        else:
            return result[0] + middle + result[1]


""" print(arrangement)

answer = quick_parallel_sort(arrangement)

print(answer)
 """