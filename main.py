# Main programm for comparing algorithms:

from functions import *
from sorting_algorithms import *


data_list = create_list_of_shuffled_lists(100, 50)

print(len(data_list))

# print(data_item) 
 
""" speed_results = speed_compare_algorithms(
    data_list, "quicksort", "quick_parallel_sort", "sorting_algorithms", "sorting_algorithms")
 """

# display_speed_comparison(speed_results, "Quicksort", "Quicksort in Parallel")