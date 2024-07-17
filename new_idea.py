# Sorting algorthim that takes a lists and automatically returns a number of sublists or stacks, each of which are sorted.
# Creating a single sorted list by  subsequently applying the merge-function on the sublists used in the merge-sort algoritm.
# Hoping that the number of merge operations is reduced.


# Defining a list of random integers:

from random import shuffle


def main():
    random_list = list(range(100))
    randome_list = shuffle(random_list)
    
    list_of_sublists = lists_of_ordered_sublists(random_list)
    
    while len(list_of_sublists) >= 2:
        right = list_of_sublists.pop()
        left = list_of_sublists.pop()
        
        new_list = merge(left, right)
        
        list_of_sublists.append(new_list)
    
    print(list_of_sublists)


def errorless_pop(liste: list):
    """Reurn None during pop, if list is empty

    Args:
        liste (list): random list

    Returns:
        Popped element, if the list is not empty
        None, if the list is empty
        Content oflist is reduced, because list
        is a mutable data type passed to the function. 
    """
    try: 
        return liste.pop()
    except IndexError:
        return None
    

def lists_of_ordered_sublists(int_list: list[int]):
    """Create listtof ordered sublists

    Args:
        int_list (list[int]): _description_

    Returns:
        list[list]: _description_
    """

    list_of_sublists = []
    pop_number = errorless_pop(int_list)


    while pop_number != None:
        if len(list_of_sublists) == 0:
            list_of_sublists.append([pop_number])
        else:
            for item in list_of_sublists:
                # append pop to end of item_list, if  pop >  last element of item
                if pop_number > item[-1]:
                    item.append(pop_number)
                    break
                # insert pop item to beginnin of list, if pop < first element of item
                elif pop_number < item[0]:
                    item.insert(0, pop_number)
                    break
            # If item was not added to any sublist, append a new sub-list, which
            # comprises as single element, namely the pop-numer
            else:
                list_of_sublists.append([pop_number])
        # Pop numbers until the list is empty
        pop_number = errorless_pop(int_list)

    return list_of_sublists



def merge(left, right):
    # If the first array is empty, then nothing needs
    # to be merged, and you can return the second array as the result
    if len(left) == 0:
        return right

    # If the second array is empty, then nothing needs
    # to be merged, and you can return the first array as the result
    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    # Now go through both arrays until all the elements
    # make it into the resultant array
    while len(result) < len(left) + len(right):
        # The elements need to be sorted to add them to the
        # resultant array, so you need to decide whether to get
        # the next element from the first or the second array
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        # If you reach the end of either array, then you can
        # add the remaining elements from the other array to
        # the result and break the loop
        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result

main()