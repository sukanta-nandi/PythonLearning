
# Ref: https://www.datacamp.com/tutorial/decorators-python
# Ref: https://realpython.com/primer-on-python-decorators/


# Function as arguments

def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def greet_bob(greeter_func):
    name = "Bob"
    return greeter_func(name)

print(greet_bob(say_hello))

print(greet_bob(be_awesome))



# Inner Function
def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()

parent()


# Returning function from function
def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child


first = parent(1) # returns ref to first child
second = parent(2) # returns ref to second child
print(first)
print(second)

print(first())
print(second())


# Simple decorators

# Decorators
def uppercase_decorator(function):
    print("Uppercase decorator funcion called")
    def wrapper():
        print(f"function: {function}")
        func_res = function()
        print(f"func res: {func_res}")
        make_uppercase = func_res.upper()
        return make_uppercase

    return wrapper


def split_string(function):
    print("split string decorator called")
    def wrapper():
        print(f"function: {function}")
        func_res = function()
        print(f"func res: {func_res}")
        splitted_string = func_res.split()
        return splitted_string

    return wrapper

@split_string
@uppercase_decorator
def say_hi():
    return 'hi there'



print(say_hi())

def say_hi_example():
    return 'hi there'

# decorate = uppercase_decorator(say_hi_example)
# print(f"uppercase wrapper: {decorate}")
# print(decorate())
#print(uppercase_decorator(say_hi)())


###### for multi decorator
# upper_decorator_wrapper = uppercase_decorator(say_hi)
# print(upper_decorator_wrapper)
# split_dec_wrapper = split_string(upper_decorator_wrapper)
# print(split_dec_wrapper)
# print("calling wrappers")
# print(split_dec_wrapper())


