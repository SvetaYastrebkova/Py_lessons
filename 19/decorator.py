def decorator(func):
    def wrapper():
        print("До вызова функции")
        func()
        print("После вызова функции")
    return wrapper

@decorator
def say_hello():
    print("Привет!")

say_hello()

def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов {func.__name__} с аргументами {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper

@decorator
def add(a, b):
    return a + b

add(3, 4)

#пример с логированием
def log(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Вызов функции {func.__name__} с аргументами {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] Функция {func.__name__} вернула {result}")
        return result
    return wrapper

@log
def add(a, b):
    return a + b

@log
def greet(name):
    return f"Привет, {name}!"

# Использование
add(5, 7)
greet("Аня")





from datetime import datetime


def my_decorator(func):

    def wrapper(n):
        print(datetime.now())
        print(f'My name is: {func(n)}')
    return wrapper


@my_decorator
def print_name(nam):
    return(nam)


print_name('Haim')
print_name('Bob')
