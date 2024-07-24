from merge_sort import merge
from random import shuffle
from multiprocessing import Pool


def return_list(old_value: int) -> list:
    return [old_value]


def kilian2_merge(new_list: list) -> list:

    with Pool() as p:
        result = p.map(return_list, new_list)

    new_list = list(result)

    while len(new_list) >= 2:
        item1 = new_list.pop(0)
        item2 = new_list.pop(0)

        new_item = merge(item1, item2)
        new_list.append(new_item)

    return new_list[0]


def main():
    numbers = list(range(1000))
    shuffle(numbers)

    result = kilian2_merge(numbers)

    print(result)


main()
