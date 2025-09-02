def f1(*args): # *args - arbitrary positional arguments
    print()
    for p in args:
        print(type(p), p)

list1 = [1,2,3,4,5]
f1(list1)
f1(22,33,44)
f1(*list1)  # * operator - unpack list(tuple)

def f2(**kwargs): # *kwargs - arbitrary keyword arguments
    print()
    for p in kwargs:
        print(type(p), p)



f2(par1 = "A", par2 = "B")
'''
<class 'tuple'> ('par1', 'A')
<class 'tuple'> ('par2', 'B')
'''

f2(par1 = "A", par2 = "B", weight = 100, height = 22)
'''
<class 'tuple'> ('par1', 'A')
<class 'tuple'> ('par2', 'B')
<class 'tuple'> ('weight', 100)
<class 'tuple'> ('height', 22)
'''

user1 = {
  "id": 1,
  "first_name": "Alika",
  "last_name": "Challace",
  "email": "achallace0@ucoz.com",
  "gender": "Female",
  "ip_address": "15.45.19.169"
}

user2 = {
  "id": 1,
  "first_name": "Tobe",
  "last_name": "Burgin"
}
f2(**user1)  # ** -> dictionary unpack
'''
<class 'tuple'> ('id', 1)
<class 'tuple'> ('first_name', 'Alika')
<class 'tuple'> ('last_name', 'Challace')
<class 'tuple'> ('email', 'achallace0@ucoz.com')
<class 'tuple'> ('gender', 'Female')
<class 'tuple'> ('ip_address', '15.45.19.169')
'''
f2(**user2)
'''
<class 'tuple'> ('id', 1)
<class 'tuple'> ('first_name', 'Tobe')
<class 'tuple'> ('last_name', 'Burgin')
'''

def f3 (*names, **properties):
# def f3 (**properties, *names): # ERROR
    print("*names")
    for p in names:
        print(type(p), p)
    print("**properties")
    for p in properties.items():
        print(type(p), p)    

f3("Haim", "Bob", prop1 = 11, prop2 = 33)

''''
Ключевые аргументы

Передаются с указанием имени параметра.

Порядок не имеет значения, так как мы явно указываем имя.    


Позиционные аргументы

Передаются по порядку, в котором они определены в функции.

Главное — позиция, а не имя.

Вызов:

Сначала позиционные,

Потом ключевые.
'''

