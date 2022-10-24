# https://www.pythonmorsels.com/map-and-filter-python/

# The map function transforms each item
# The map function accepts a function and an iterable.
# The map function returns a lazy iterable:

from typing import Iterable


def square(x):
    return x**2


def is_odd(x):
    return x%2 != 0


from functools import reduce

def add(x, y):
    return x + y




numbers = [2, 1, 3, 4, 7, 11, 18]

# lazy iterable
map_result = map(square, numbers)

filter_result = filter(is_odd, numbers)

print(f"Map Result: {list(map_result)}")
print(f"Filter Result: {list(filter_result)}")
print(f"Reduce Result: {reduce(add, numbers)}")



# map and filter are equivalent to writing a generator expression
# The map function takes each item in a given iterable and and includes all of them in a new lazy 
# iterable, transforming each item along the way
# The filter function doesn't transform the items, but it's selectively picks out which items it should 
# include in the new lazy iterable
# The reason I don't usually recommend using map and filter is that they can each be summed up in just 
# one line of Python code.

# Using Generator

def map(function, iterable):
    return (function(x) for x in iterable)


def filter(function, iterator):
    return (x for x in iterator if function(x))

gen_map_result = map(square, numbers)
gen_filter_result = filter(is_odd, numbers)

print(f"Generator Map Result: {list(gen_map_result)}")
print(f"Generator Filter Result: {list(gen_filter_result)}")
