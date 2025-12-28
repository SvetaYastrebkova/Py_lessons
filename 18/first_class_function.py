# functions in Python: first-class-objects
'''
- assign to variabes
- passed as arguments
- use in return statements
- use in datastructures

'''

# - assign to variabes
def f1():
    print ("F1 called")
    pass
a = f1
print(type(a))
print(id(f1))
print(id(a))
a()

def f2(s:str, worker = lambda p: p) -> None:
    print(worker(s))
    pass

def w1(p):
    return 10 * p

def w2(p):
    return len(p)

# - passed as arguments
f2("Test string ", w1)
f2("Test string ", w2)
f2("Test string ")

'''
Test string Test string Test string Test string Test string Test string Test string Test string Test string Test string
12
Test string
'''

def multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = multiplier(2)
triple = multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

operations = [add, subtract]  # список функций

for op in operations:
    print(op(10, 5))  
# Output:
# 15
# 5

# В словаре
ops_dict = {"plus": add, "minus": subtract}
print(ops_dict["plus"](7, 3))   # 10
print(ops_dict["minus"](7, 3))  # 4
