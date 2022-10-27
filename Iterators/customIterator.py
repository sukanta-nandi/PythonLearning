# # https://www.programiz.com/python-programming/iterator
# https://www.geeksforgeeks.org/python-difference-iterable-iterator/


def is_iterable(ob):
  try:
      iter(ob)
      return True
  except TypeError:
      return False

class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


# create an object
numbers = PowTwo(3)

print(numbers)
print(f"Is Iterable: {is_iterable(numbers)}")

# create iterator
iterator = iter(numbers)

print(f"Iterator: {iterator}")
print(f"Next element: {next(iterator)}")
print(f"Next element: {next(iterator)}")
print(f"Next element: {next(iterator)}")
print(f"Next element: {next(iterator)}")
# print(f"Next element: {next(iterator)}") # StopIteration Error


# behind the scene it calls iter()
# and also calls next()
for num in PowTwo(3):
    print(f"Pow Two Num: {num}")