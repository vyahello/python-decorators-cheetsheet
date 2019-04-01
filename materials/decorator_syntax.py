def trace(func):
    def wrapper():
        func_name = func.__name__
        print(f'Entering "{func_name}" function')
        result = func()
        print(f'Result of "{func_name}" function is {result}')
        print(f'Exiting from "{func_name}" function')
        return result
    return wrapper


@trace
def say_hello():
    return 'Hello!'


say_hello()
