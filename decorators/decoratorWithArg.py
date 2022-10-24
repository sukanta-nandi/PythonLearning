# Decorator with arguments


def uppercase_decorator(function):
    print("Called uppercase decorator")

    def uppercase_wrapper(*args, **kwargs):
        print(f"function: {function}")
        func_res = function(*args, **kwargs)
        print(f"func res: {func_res}")
        make_uppercase = func_res.upper()
        return make_uppercase

    return uppercase_wrapper


def split_line_decorator(function):
    print("Split line decorator called")
    
    def split_line_wrapper(*args, **kwargs):
        print(f"function: {function}")
        func_res = function(*args, **kwargs)
        print(f"func res: {func_res}")
        splitted_line = func_res.split('.')
        return splitted_line

    return split_line_wrapper


@split_line_decorator
@uppercase_decorator
def greet(name, age=20):
    return (f"hi {name}. You are {age} years old")


print(greet("Bob", age=18))


def greet_example(name, age=20):
    return (f"hi {name}. You are {age} years old")




uppercse_wrapper = uppercase_decorator(greet_example)
print(f"uppercase wrapper: {uppercse_wrapper}")
print(uppercse_wrapper("Bob", age=18))
###print(uppercse_wrapper(greet_example)())    



###### for multi decorator
upper_decorator_wrapper = uppercase_decorator(greet_example)
print(upper_decorator_wrapper)
split_dec_wrapper = split_line_decorator(upper_decorator_wrapper)
print(split_dec_wrapper)
print("calling wrappers")
print(split_dec_wrapper("Bob", age=18))


