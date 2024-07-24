from lists_of_ordered_sublists import lists_of_ordered_sublists
from merge_sort import merge
from random import shuffle


def main():

    # Create unsortedlist
    shuffled_list = list(range(10000))
    shuffle(shuffled_list)

    # Call kilian_merge()

    ordered_list = kilian1_merge(shuffled_list)

    print(ordered_list)


def kilian1_merge(new_list):

    # Create a list of ordered sublists:
    new_lists = lists_of_ordered_sublists(new_list)

    # Merge the ordered sublists in order to create an ordered list using merge()
    while len(new_lists) >= 2:
        right = new_lists.pop()
        left = new_lists.pop()
        interim_list = merge(left, right)
        new_lists.append(interim_list)

    return new_lists[0]


if __name__ == "__main__":
    main()
