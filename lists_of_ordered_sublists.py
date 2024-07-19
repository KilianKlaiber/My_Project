# Create a list of ordered sublists out of an unordered list.
# All items of the list are consecutively popped.
# If the item belongs to the end or beginning of a sublist,
# The item will be inserted into said sublist.
# Else, a new sublist is created with the item as single item of the
# sublist.


def main():
    from random import shuffle

    new_list = list(range(1000))
    shuffle(new_list)

    lists = lists_of_ordered_sublists(new_list)

    print("number of lists: ", len(lists))
    print("*" * 100)
    print("list of sublists: ", lists)


def lists_of_ordered_sublists(int_list: list[int]):
    """Create list of ordered sublists

    Args:
        int_list (list[int]): List of integers, which are not sorted.

    Returns:
        list[list]: List of sublist. Each sublist is sorted. The sublists taken together
        contain all the items of the intput list of integers.
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


def errorless_pop(liste: list):
    """Return None during pop, if list is empty

    Args:
        liste (list): random list

    Returns:
        Popped element, if the list is not empty
        None, if the list is empty
        Content of list is reduced without returning the list, 
        because list is a mutable data type passed to the function.
    """
    try:
        return liste.pop()
    except IndexError:
        return None


if __name__ == "__main__":
    main()
