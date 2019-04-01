def trace(func):
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        print(f'Entering "{func_name}" function')
        print(f'"{func_name}" function takes [{args}, {kwargs}] args')
        result = func(*args, **kwargs)
        print(f'Result of "{func_name}" function is "{result}"')
        print(f'Exiting from "{func_name}" function')
        return result
    return wrapper


@trace
def say_hello_to(word):
    return f'Hello {word}!'


say_hello_to('Python')
