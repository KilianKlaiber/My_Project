# Sorting algorthim that takes a lists and automatically returns a number of sublists or stacks, each of which are sorted.
# Creating a single sorted list by  subsequently applying the merge-function on the sublists used in the merge-sort algoritm.
# Hoping that the number of merge operations is reduced.


# Defining a list of random integers:

from random import shuffle

random_list = list(range(500))

randome_list = shuffle(random_list)


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
    

def list_to_list_of_ordered_sublists(int_list: list[int]):
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


new_list = list_to_list_of_ordered_sublists(random_list)

length_new_list = len(new_list)

print("length of new list: ", length_new_list)

print("new list: ", new_list)


