
square = lambda x: x * x
print(square(5))  # 25

# то же самое обычной функцией
def square(x):
    return x * x

print(square(5))  # 25


print((lambda a, b: a+b) (2,3))

# 1
def outer():
    x = 5
    def inner():
        nonlocal x
        x += 1
        print(x)
    inner()
outer()
# 2
def outer():
    x = 5
    def inner():
        x = 1
        x += 1
        print(x)
    inner()
outer()
# 3
def outer():
    x = 5
    def inner():
        x += 1
        print(x)
    inner()
outer()