from multiprocessing import Pool
from merge_sort import merge, merge_sort
from lists_of_ordered_sublists import lists_of_ordered_sublists
from random import shuffle
import time

def merge_wrapper(args):
    return merge(*args)

if __name__ == '__main__':
    new_list = list(range(100000000))
    shuffle(new_list)
    
    start_time = time.time()
    merge_sort(new_list)
    end_time = time.time()
    delta_time = end_time - start_time
    print("mergesort", delta_time)
    
    start_time = time.time()
    
    list_of_lists = [[x] for x in new_list]
      
    while len(list_of_lists) >= 2:
        
        length = len(list_of_lists)
        
        # Combine the two lists into a single list of tuples
        args = list(zip(list_of_lists[:length//2], list_of_lists[length//2:]))

        with Pool() as p:
            list_of_lists = p.map(merge_wrapper, args)
    end_time = time.time()
    delta_time = end_time - start_time
    print("kiliansort", delta_time)
  
        
        
    
