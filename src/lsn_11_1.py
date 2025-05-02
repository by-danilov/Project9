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
# from curses.ascii import isalpha

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

# def is_even(x):
#     return x % 2 == 0
#
# result_filter = list(filter(is_even, range(21)))
#
#
# def duplicate(x):
#     return [x, x]
#
# result_map = list(map(duplicate, result_filter))
#
# from itertools import chain
#
# result_chain = list(chain(*result_map))
#
# print(result_chain)


# ascii_codes = [ord(c) for c in "Hello" if c.isalpha() and c.islower()]
# print(ascii_codes)
#
#
# matching_indices = [i for i, (x, y) in enumerate([(1, 2), (4, 4), (5, 7), (0, 0)]) if x == y]
# print(matching_indices)


# numbers = range(1, 101)
# result = [x for x in numbers if x % 3 == 0 or x % 5 == 0]
# print(result)


# def print_6(xs):
#     for i, x in enumerate(xs):
#         print(x)
#         if i == 5:
#             break
#
#
# i = (x * x for x in range(10))
# print_6(i)
# print('#' * 5)
# print_6(i)
# print('#' * 5)
# print_6(i)


# result = (x * x for x in range(1, 101) if x % 2 == 0)
# print(sum(result))


# print(*(x for x in "Hello World!" if x.isupper()))

# cubes = (x**3 for x in range(11) if x % 2 == 0)


# def sum_of_squares(lst):
#     return sum(x**2 for x in lst if x > 0)


# letters = (x for x in "hello" if x in ['a', 'e', 'i', 'o', 'u'])


# def inf_seq(start=1):
#     while True:
#         yield start
#         start += 1
#
#
# numbers = inf_seq()
#
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))


# def generate_numbers_up_to_100():
#     for i in range(1, 101):
#         yield i
#
# for number in generate_numbers_up_to_100():
#     print(number)



