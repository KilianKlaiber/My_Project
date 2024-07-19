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

# Example usage:
unsorted_list = [34, 7, 23, 32, 5, 62]
sorted_list = merge_sort(unsorted_list)
print(sorted_list)  # Output: [5, 7, 23, 32, 34, 62]
