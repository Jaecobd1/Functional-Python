from functools import reduce

wizard = {
    'name': 'Merlin',
    'power': 50
}

my_list = [1, 2, 3]
your_list = [10, 20, 30]


def attack(character):
    print("attacking...")


def multiply_by2(item):
    return (item * 2)


def check_odd(item):
    return item % 2 != 0


def accumulator(acc, item):
    print(acc, item)
    return acc + item


# map, filter, zip and reduce
print(reduce(accumulator, my_list, 0))
print(my_list)
