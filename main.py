# Main programm for comparing algorithms:

from functions import *
from sorting_algorithms import *

data_list = create_list_of_shuffled_lists(300, 50)

speed_results = speed_compare_algorithms(
    data_list, "quicksort", "quick_parallel_sort", "sorting_algorithms", "sorting_algorithms")

print(speed_results)


display_speed_comparison(speed_results, "quicksort", "quick_parallel_sort")
