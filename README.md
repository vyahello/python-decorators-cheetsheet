# Python decorators cheetsheet
Implementation of python decorators cheetsheet which is aimed on helping to comprehend python decorators by newcomers.

## Table of contents
- [Write a decorator](#write-a-decorator)
- [Decorator syntax](#decorator-syntax)
- [Decorate functions with arguments](#decorate-functions-with-arguments)
- [Decorate classes and class methods](#decorate-classes-and-class-methods)
- [Preserve metadata with decorators](#preserve-metadata-with-decorators)
- [Define a decorator that takes arguments](#define-a-decorator-that-takes-arguments)
- [Nested decorators](#nested-decorators)
- [Additional materials](#additional-materials)

### Write a decorator
```python
# decorator.py

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
```

### Decorator syntax
```python
# decorator_syntax.py

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
```

### Decorate functions with arguments
```python
# function_with_args.py

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
```

### Decorate classes and class methods
Decorate a class
```python
# decorate_class.py

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
```

Decorate a class method
```python
# decorate_class_method.py

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
```

### Preserve metadata with decorators
```python
from functools import wraps

help(wraps)
```

```python
# not_preserved_metadata.py

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
    """Return `Hello!` string."""
    return 'Hello!'


help(say_hello)
print(say_hello.__doc__)
print(say_hello.__name__)
```


```python
# preserved_metadata.py

from functools import wraps


def trace(func):
    @wraps(func)
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
    """Return `Hello!` string."""
    return 'Hello!'


help(say_hello)
print(say_hello.__doc__)
print(say_hello.__name__)
```

### Define a decorator that takes arguments
```python
# decorator_with_args.py

from functools import wraps


def multiply_by(multiplier):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_name = func.__name__
            print(f'Calling "{func_name}({args[0]}, {args[1]})" function')
            print(f'"{func_name}" function is multiplied by {multiplier}')
            result = func(*args, **kwargs) * multiplier
            print(f'Result equals to {result}')
            return result
        return wrapper
    return decorator


@multiply_by(multiplier=3)
def add(a, b):
    return a + b


add(2, 3)
```

### Nested decorators
```python
# nested_decorators.py

from functools import wraps


def multiply_by(multiplier):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_name = func.__name__
            print(f'Calling "{func_name}({args[0]}, {args[1]})" function')
            print(f'"{func_name}" function is multiplied by {multiplier}')
            result = func(*args, **kwargs) * multiplier
            print(f'Result equals to {result}')
            return result
        return wrapper
    return decorator


@multiply_by(multiplier=3)
@multiply_by(multiplier=4)
def add(a, b):
    return a + b


add(2, 3)
```

### Additional materials
- http://book.pythontips.com/en/latest/decorators.html
- https://www.python-course.eu/python3_decorators.php
- https://realpython.com/primer-on-python-decorators/#syntactic-sugar

# Contributing
- clone the repository
- configure Git for the first time after cloning with your name and email
  ```bash
  git config --local user.name "Volodymyr Yahello"
  git config --local user.email "vyahello@gmail.com"
  ```
- `python3.6` is required to run the code

