# Sorting algorthim that takes a lists and automatically returns a number of sublists or stacks, each of which are sorted.
# Creating a single sorted list by  subsequently applying the merge-function on the sublists used in the merge-sort algoritm.
# Hoping that the number of merge operations is reduced.


# Defining a list of random integers:

int_list = [400, 1000, 2000, 900, 532]


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
    


list_of_sublists = []

pop_number = errorless_pop(int_list)


while pop_number != None:
    if len(list_of_sublists) == 0:
        list_of_sublists.append([pop_number])
    else:
        for item in list_of_sublists:
            if pop_number > item[-1]:
                item.append(pop_number)
                break
            elif pop_number < item[0]:
                print("item before: ", item)
                item.insert(0, pop_number)
                break
        else:
            list_of_sublists.append([pop_number])
    pop_number = errorless_pop(int_list)

print(list_of_sublists)


                
   
