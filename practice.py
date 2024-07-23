from multiprocessing import Pool
from merge_sort import merge, merge_sort
from lists_of_ordered_sublists import lists_of_ordered_sublists
from random import shuffle
import time



if __name__ == '__main__':
    new_list = list(range(10))
    shuffle(new_list)
    
    start_time = time.time()
    merge_sort(new_list)
    end_time = time.time()
    delta_time = end_time - start_time
    print("Merge-sort", delta_time)
    
    
    start_time = time.time()
    while len(new_list) >= 2:
        
       item1 = new_list.pop(0)
       if not isinstance(item1,list):
           item1 = [item1]
       
       item2 = new_list.pop(0)
       if not isinstance(item2,list):
           item2 = [item2]
       
       new_item = merge(item1, item2)
       new_list.append(new_item)
    
    end_time = time.time()
    delta_time = end_time - start_time
    print("NewMerge-Sort", delta_time)
    
    print(new_list)
       
       
       
       # pop two elements.
       # check if both elements are lists, if not turn them into lists
       # merge both elemts using merge function.
       # append the merge to the original list.

"""         with Pool() as p:
            list_of_lists = p.map(merge_wrapper, args)
     """
