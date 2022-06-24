wizard = {
    'name': 'Merlin',
    'power': 50
}

my_list = [1, 2, 3]


def attack(character):
    print("attacking...")


def multiply_by2(item):
    return (item * 2)


def check_odd(item):
    return item % 2 != 0


# map, filter, zip and reduce
print(list(filter(check_odd, my_list)))
print(my_list)
