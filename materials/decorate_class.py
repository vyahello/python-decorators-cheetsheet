def trace(cls):
    def wrapper(*args, **kwargs):
        class_name = cls.__name__
        print(f'Entering "{class_name}" class')
        print(f'"{class_name}" class takes [{args}, {kwargs}] args')
        cls(*args, **kwargs)
        print(f'Exiting from "{class_name}" class')
    return wrapper


@trace
class Hello:
    def __init__(self):
        print(f'Initializing "{self.__class__.__name__}" object')


Hello()
