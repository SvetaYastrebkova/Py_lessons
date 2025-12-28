# map() - transform elements

from functools import reduce

res1 = map(lambda x: x**2, [1,2,3,4,5])
print(list(res1))
print(list(map(lambda p: str(p), [1,2,3,4,5])))

# new_list  = []
# for next_item in [1,2,3,4,5]:
#     new_list.append(str(next_item))
#     pass

print(list(map(lambda p: str(p), [1,2,3,4,5])))

# filter filtering, select elements
res = filter(lambda e: e % 2 == 0, [1,2,3,4,5,6,7,8,9])
print (list(res))

# sorted -> sort
res = sorted([1,2,6,7,8,93,4,5,-66], key = lambda e: -e)
print(list(res)) # [93, 8, 7, 6, 5, 4, 2, 1, -66]

res = sorted("Test String", key = lambda s: ord(s))
print(list(res))

user = {
  "id": 1,
  "first_name": "Vaclav",
  "last_name": "Redford",
  "email": "vredford0@ustream.tv",
  "gender": "Male",
  "ip_address": "175.230.134.142"
}

res = sorted(user.keys(), key = lambda s: len(s))
print(list(res))

# reduce convert to single value

def worker(p1,p2):
    print(p1)
    return p1+p2

print(reduce(lambda e1,e2 : e1*e2,  [1,2,3,4,5,6,7,8,9]))
print(reduce(lambda e1,e2 : e1+e2,  [1,2,3,4,5,6,7,8,9]))

# 
print(reduce(lambda e1,e2, f = worker: f(e1,e2),  [1,2,3,4,5,6,7,8,9]))

# reduce recieved reference to ne anonymous function wit 2 parameters e1,e2 and function body: worker(e1,e2) 
# interpreter does not execute lambda e1,e2: worker(e1,e2)
# reduce calling this function 8 timess, e1 - previous call, e2 - next item
print(reduce(lambda e1,e2: worker(e1,e2),  [1,2,3,4,5,6,7,8,9]))
# print(reduce(worker(e1,e2),  [1,2,3,4,5,6,7,8,9])) # NameError: name 'e1' is not defined
print(reduce(worker,  [1,2,3,4,5,6,7,8,9]))

# min, max
print(min([1,2,3,4,5,6,7,8,9], key=lambda e: -e))
print(min("[1,2,3,4,5,6,7,8,9]", key=lambda e: e))
