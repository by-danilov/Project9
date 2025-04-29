# for i in range(10):
#     print(i)
#
#
# for i in [1, 2, 3, 4, 5, 6,  7, 8]:
#     print(i)
#
#
# for i in "12345678":
#     print(i)

# def is_even(x):
#     return x % 2 == 0
#
# def add_two(x):
#     return x + 2
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = list(filter(is_even, numbers))
# result = list(map(add_two, even_numbers))
# print(result

def is_even(x):
    return x % 2 == 0

result_filter = list(filter(is_even, range(21)))


def duplicate(x):
    return [x, x]

result_map = list(map(duplicate, result_filter))

from itertools import chain

result_chain = list(chain(*result_map))

print(result_chain)
