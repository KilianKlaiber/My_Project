# Main programm for comparing algorithms:

from functions import *
from sorting_algorithms import *
import time

data_list = create_list_of_shuffled_lists(100, 500)



speed_results = speed_compare_algorithms(
    data_list, "quick_parallel_sort", "quicksort", "sorting_algorithms", "sorting_algorithms")


display_speed_comparison(speed_results, "quick_parallel_sort", "quicksort")