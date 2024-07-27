# Main programm for comparing algorithms:

from functions import *
from sorting_algorithms import *
import time

#data_list = create_list_of_shuffled_lists(10000, 500)

def wait(x):
    time.sleep(5)
    return x

data_list = [5]

speed_results = speed_compare_algorithms(
    data_list, "wait", "wait", "main", "main")


display_speed_comparison(speed_results, "quick_parallel_sort", "quicksort")