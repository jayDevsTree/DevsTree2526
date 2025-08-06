import time

# args and kwargs example
def my_decorator(func):
    def banana(*args, **kwargs):  # name can be anything
        print("Before function")
        result = func(*args, **kwargs)
        print("After function")
        return result
    return banana

@my_decorator
def say_hello():
    print("Hello!")

say_hello()


# this shows basic decorator
def log_arguments(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_arguments
def add(a, b):
    return a + b

print(add(3, 5))


# this run twice using decorator which return type of function
def run_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper

@run_twice
def greet(name):
    print(f"Hello {name}")

greet("Jay")



# static method
class Example: # not need self or cls methods
    @staticmethod
    def greet():
        print("Hello from static method")

Example.greet()

# class method
def add_class_info(cls):
    cls.info = "This is a decorated class"
    return cls

@add_class_info
class MyClass:
    pass

print(MyClass.info)

def run_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)           # First call
        return func(*args, **kwargs)    # Second call, and its result is returned
    return wrapper

@run_twice
def greet(name):
    print(f"Hello {name}")

greet("Jay")



# # static and class method
# class Example:
#     @staticmethod
#     def say_hello():
#         print("Hello from static method")

#     @classmethod
#     def say_class(cls):
#         print("Hello from", cls.__name__)

# Example.say_hello()
# Example.say_class()



# property(Getter and Setter)

class Student:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):  # Getter
        return self._name

    @name.setter
    def name(self, value):  # Setter
        if not value.isalpha():
            raise ValueError("Name must contain only letters")
        self._name = value

s = Student("Jay")
print(s.name)     # Getter called
s.name = "Veer"   # Setter called
print(s.name)     # Getter called again

# this is a timer decorator
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.2f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    print("Finished!")

slow_function()
