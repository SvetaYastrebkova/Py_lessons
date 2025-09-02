

collection3 = {1,2,3,2,3,1}
# set
print(len(collection3)) # 3 !!!!!


def f1(l:list): # 
    l.append("New item")

    pass
# f1(collection3) # AttributeError: 'set' object has no attribute 'append'
f1(list(collection3)) # 
print(collection3) # {1, 2, 3}

c3 = list(collection3)
f1(c3)
print(c3)

def f2(l:list): # 
    l = [] 
    pass

c3 = [1,2,3]
f2(c3)
print(c3)
