def trace(method):
    def wrapper(*args, **kwargs):
        method_name = method.__name__
        class_name = args[0].__class__.__name__
        print(f'Entering "{method_name}" method in "{class_name}" class instance')
        print(f'"{method_name}" class method takes [{args}, {kwargs}] args')
        result = method(*args, **kwargs)
        print(f'Result of "{method_name}" method in "{class_name}" class instance is {result}')
        print(f'Exiting from "{method_name}" method in "{class_name}" class instance')
        return result
    return wrapper


class Hello:
    def __init__(self, word):
        self._word = word

    @trace
    def say(self):
        return f'Hello {self._word}!'


hello = Hello('Python')
hello.say()
