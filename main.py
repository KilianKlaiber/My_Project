# Main programm for comparing algorithms:

from functions import *
from sorting_algorithms import *
""" 
algo1 = input("Chose first algorithm: ")
algo2 = input("Chose second algorithm: ")
data_list = input("json_file comprising list of unsorted lists")

data_list = read_from_json(data_list)
 """
 




data = create_list_of_shuffled_lists(500, 50)

# print(data_item) 
 
""" speed_results = speed_compare_algorithms(
    data_list, quicksort, quick_parallel_sort, "sorting_algorithms", "sorting_algorithms")

display_speed_comparison(speed_results, algo1, algo2)

results_json = input("Name json-file for storing measurement results:")

save_speed_comparison(speed_results, results_json) """