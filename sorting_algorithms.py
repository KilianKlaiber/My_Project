# Collection of Merging Algorithms:

from multiprocessing import Pool
from functions import parallel_process
from random import shuffle


def main():
    numbers = list(range(1000))
    shuffle(numbers)
    result = merge_direct(numbers)
    
    print(result)
#############################################################################


# Quicksort:
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)
############################################################################


def quick_parallel_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        
        result = parallel_process(quick_parallel_sort, [left, right])
        if result != None:
            return result[0] + middle + result[1]
            
        else:
            print("Parallel Processing failed!")
            return None
           
##########################################################################


# Merge_Sort_Recursive:
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):
    sorted_arr = []
    left_index = 0
    right_index = 0

    # Merge the two lists until one is empty
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_arr.append(left[left_index])
            left_index += 1
        else:
            sorted_arr.append(right[right_index])
            right_index += 1

    # Append any remaining elements from the left or right list
    sorted_arr.extend(left[left_index:])
    sorted_arr.extend(right[right_index:])

    return sorted_arr
####################################################################################


# Merge_parallel_Sort_Recursive:
def merge_parallel_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves simultaneously
    result = parallel_process(merge_parallel_sort, [left_half, right_half])
    
    if result != None:
        # Merge the sorted halves
        return merge(result[0], result[1])
    else:
        print("Parallel Processing failed!")
        return None
        
##############################################################################


# Merge_Ordered_Sublists:
def merge_ordered_sublists(new_list):

    # Create a list of ordered sublists:
    new_lists = lists_of_ordered_sublists(new_list)

    # Merge the ordered sublists in order to create an ordered list using merge()
    while len(new_lists) >= 2:
        right = new_lists.pop()
        left = new_lists.pop()
        interim_list = merge(left, right)
        new_lists.append(interim_list)

    return new_lists[0]


def lists_of_ordered_sublists(int_list: list[int]):
    """Create list of ordered sublists

    Args:
        int_list (list[int]): List of integers, which are not sorted.

    Returns:
        list[list]: List of sublist. Each sublist is sorted. The sublists taken together
        contain all the items of the intput list of integers.
    """

    list_of_sublists = []
    pop_number = errorless_pop(int_list)

    while pop_number != None:
        if len(list_of_sublists) == 0:
            list_of_sublists.append([pop_number])
        else:
            for item in list_of_sublists:
                # append pop to end of item_list, if  pop >  last element of item
                if pop_number > item[-1]:
                    item.append(pop_number)
                    break
                # insert pop item to beginnin of list, if pop < first element of item
                elif pop_number < item[0]:
                    item.insert(0, pop_number)
                    break
            # If item was not added to any sublist, append a new sub-list, which
            # comprises as single element, namely the pop-numer
            else:
                list_of_sublists.append([pop_number])
        # Pop numbers until the list is empty
        pop_number = errorless_pop(int_list)

    return list_of_sublists


def errorless_pop(liste: list):
    """Return None during pop, if list is empty

    Args:
        liste (list): random list

    Returns:
        Popped element, if the list is not empty
        None, if the list is empty
        Content of list is reduced without returning the list, 
        because list is a mutable data type passed to the function.
    """
    try:
        return liste.pop()
    except IndexError:
        return None
################################################################################


# Merge_direct:
def merge_direct(new_list: list) -> list:

    with Pool() as p:
        result = p.map(return_list, new_list)

    new_list = list(result)

    while len(new_list) >= 2:
        item1 = new_list.pop(0)
        item2 = new_list.pop(0)

        new_item = merge(item1, item2)
        new_list.append(new_item)

    return new_list[0]

def return_list(old_value: int) -> list:
    return [old_value]
###################################################################################


if __name__ == "__main__":
    
    main()