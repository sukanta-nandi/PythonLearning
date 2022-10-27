

# https://docs.python.org/3/tutorial/classes.html#iterators

# When we use for loop we create an iterator by passing the iterable
# Iterator is something that implements the __next__ and helps us to 
# loop through one element at a time

# we can create iterator using iter(iterable)

s = 'abc'

iterator = iter(s)

# print iterator
print(f"Iterator: {iterator}")

print(f"Next element: {next(iterator)}")
print(f"Next element: {next(iterator)}")
print(f"Next element: {next(iterator)}")
print(f"Next element: {next(iterator)}")



