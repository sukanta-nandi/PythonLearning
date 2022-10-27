# Ref: https://www.geeksforgeeks.org/generators-in-python/
# Ref: https://www.programiz.com/python-programming/generator


# A generator function that yields 1 for first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
	yield 1		
	yield 2		
	yield 3		

# Driver code to check above generator function
for value in simpleGeneratorFun():
	print(value)


def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3
  
# x is a generator object
x = simpleGeneratorFun()
 
# print(list(x))

# for v in x:
#     print(f"v: {v}")

# Iterating over the generator object using next
print(next(x)) # In Python 3, __next__()
print(next(x))
print(next(x))


# A simple generator for Fibonacci Numbers
def fib(limit):
     
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1
 
    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b


for x in fib(50):
    print(x, end=" ")
print()


# Run without limit
# A simple generator for Fibonacci Numbers
def fib2(n):
     
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1
    count = 0
    
    # One by one yield next Fibonacci Number
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


nfib = fib2(10)
print("N fibonacci numbers")
for fibnum in nfib:
    print(fibnum, end=" ")