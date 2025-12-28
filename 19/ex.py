# 1
def outer():
    x = 5
    def inner():
        nonlocal x
        x += 1
        print(x)
    inner()
outer()

''''
В outer есть x = 5.

В inner мы пишем nonlocal x → значит, что переменная x берётся из области видимости outer (enclosing scope).

x += 1 → теперь x = 6.

Печать: 6.


'''
# 2
def outer():
    x = 5
    def inner():
        x = 1
        x += 1
        print(x)
    inner()
outer()

''''
В inner мы создаём свою локальную переменную x, которая перекрывает x из outer.

x = 1, потом x += 1 → 2.

Глобальная и enclosing x никак не тронуты.
'''
# 3
def outer():
    x = 5
    def inner():
        x += 1
        print(x)
    inner()
outer()

'''
Тут нет nonlocal, и мы не присваиваем x до x += 1.

Python считает, что x внутри inner — это локальная переменная.

Но мы пытаемся использовать её (x += 1) до присваивания.

В результате:UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
'''