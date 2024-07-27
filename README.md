# Timing Sorting Algorithms.

Write an original sorting algorithm. Compare the sorting algorithm with
merge-sort and the default algorithm sorted() in python. Display graphs
of speed measurements as a result.

The sorting Algorithms can be found in sorting_algorithms.py. Among the sorting algorithms used for speed measurment are:

# I Sorting Algorithms

## 1. Quicksort:

## def quicksort()

Classical recursive algorithm, which sorts the larger and smaller elements of the sequence to the left and right of an arbitrary pivoting point. This approach is then reapplied to the left sequence and right sequence.

## 2. Quick-parallel-sort:

## def quick_parallel_sort()

Parallel processing is applied to the recursive sorting algorithm by letting both the sorting of the left and right sequences by performed simultaneously.

## 3. Mergesort:

## def merge_sort()

Classical merging algorithm. THe algorithm either returns a value if the sequence only has one element or splits the sequence into two halves and then does the same to the halved sequences. If the halves consist both of only one element, then the result is merged using the merge function. Otherwise the halves are themselves halved until the subsequences merely consist of one element. 

The merge function merges two ordered sequences into one ordered sequence. This is done by running through both sequences from left to right simultaneously. The items from each sequence are compared and the smaller item is removed from one of the sequences and added to the merged sequence until all items have been added to the merged sequence.

## 4. Merge_parallel_Sort:

## merge_parallel_sort()

The classical mergesort algorithm is parallelized by performing the sorting algorithm  to the halved sequences simultaneously.

## 5. Merge Ordered Sublists:

## merge_ordered_sublists()

Adaptation of the mergesort algorithm. Instead of recursively splitting the sequence into its constituents before merging them, the sequence is split into ordered subsequences while it is split. This is accomplished by the functions list_of_ordered_sublists(). All the items of the list are either placed on the top or the bottom of the latest sublist. If this is not possible, then a new sublist is created.

The ordered sublists are merged using the merge function from the merge algorithm.

## 6. Merge Directly:

## merge_direct()

The merge function is applied directly to the elements of the sequence consecutively without recursively breaking up the sequence. The first two elements of the sequence are merged and this merged sequence is appended to the end of the original sequence until the sequence has only a single element.

# II. Functions

## 1. Parallel Processing

## def parallel_process()

If a single function is supposed to consecutively process a list of data as arguments, then parallel_process lets you perform this simultaneously. Parallel Processing returns the result of processing the data with the function as a list.


## 2. Compare the performance of algorithms.

## def speed_compare_algorithms()

Let two different algorithms run on the same set of data. Return the time for executing the algorithms for said data in a list of tuples.

## 3. Save performance measurments

## def save_speed_comparison()

Save the result of the speed comparison in a JSON-File

## 4. Retrieve data of performance measurements

## read_speed_comparison()

Read the data from the above JSON-File 

## 5. display_speed_comparison()
