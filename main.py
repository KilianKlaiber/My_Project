# Main programm for comparing algorithms:

from functions import *
from sorting_algorithms import *


data_list = create_list_of_shuffled_lists(2000, 500)

speed_results = speed_compare_algorithms(
    data_list, "merge_sort", "quicksort", "sorting_algorithms", "sorting_algorithms")


display_speed_comparison(speed_results, "merge_sort", "quicksort")