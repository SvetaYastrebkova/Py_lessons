#глобальные и локальные переменные

# locals() , globals(), vars()  functions

a = 11

def f1(c):
    d = 33
    print("From f1 function")
    print(locals())
    '''
    From f1 function
    {'c': 55, 'd': 33}
    '''
    pass

f1(55)

print(globals()) # module globals

print("vars")
#print(vars([]))
'''
from script2 import a, get_a

# Global scope

a = 222 # creating a in script1 global scope

def f1(): # Local f1 function scope
    global a
    a = 11 # Local variable (without global keyword)
    print(f'Inside function f1: {a =}  {id(a)=}')
    pass
print(f'Script1 global scope before f1 call: {a =}  {id(a)=}')
f1()
print(f'Script1 global scope after f1 call: {a =}  {id(a)=}')
# print(globals())
print()
get_a()

Module script2
Script1 global scope before f1 call: a =222  id(a)=140705116741448
Inside function f1: a =11  id(a)=140705116734696
Script1 global scope after f1 call: a =11  id(a)=140705116734696

Script2 global scope: a =33  id(a)=140705116735400
'''

