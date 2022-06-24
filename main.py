from functools import reduce

wizard = {
    'name': 'Merlin',
    'power': 50
}


my_list = [1, 2, 3]
your_list = [10, 20, 30]


def attack(character):
    print("attacking...")


def check_odd(item):
    return item % 2 != 0


def accumulator(acc, item):
    print(acc, item)
    return acc + item


# map, filter, zip and reduce
print(list(map(lambda item: item*2, my_list)))
print(my_list)
