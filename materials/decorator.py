def trace(func):
    def wrapper():
        func_name = func.__name__
        print(f'Entering "{func_name}" function')
        func()
        print(f'Exiting from "{func_name}" function')
    return wrapper


def say_hello():
    print('Hello!')


say_hello = trace(say_hello)
say_hello()
