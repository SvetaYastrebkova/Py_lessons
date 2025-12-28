#nested function
# E - Enclosing



a = 0
def f1():
    a = 1
    def f1_1():
        global a
        a = 2
        print(f'From f1_1 {a=} , {id(a)=}')
        pass
    f1_1()
    print(f'From f1 {a=} , {id(a)=}')
    pass

print(f'From global scope {a=} , {id(a)=}')
f1()

print(f'From global scope {a=} , {id(a)=}')



# nested functions
# E - Enclosing
# int, float, str, -> immutable

a = 0 
def f1():
    a = 1
    def f1_1():
        nonlocal a # enclosing
        a = 2
        print(f'From f1_1 {a=} , {id(a)=}')
        pass
    print(f'From f1 before f1_1 call {a=} , {id(a)=}')    
    f1_1()
    print(f'From f1 after f1_1 call {a=} , {id(a)=}')
    pass


print(f'From global scope - before f1 call {a=} , {id(a)=}')
f1()
print(f'From global scope - after f1 call {a=} , {id(a)=}')


