
'''

list
tuple
set  (frozenset)  -> {}
dictionary - Key-value pairs -> {}

'''

a = {}
print(type(a)) # <class 'dict'>
a = {1, 2}
print(type(a)) # <class 'set'>

user = {
    "name": "Haim",
    # KEY   VALUE
    "age":   33,
    # KEY   VALUE
}
print(type(user))
print(user)
'''
<class 'dict'>
{'name': 'Haim', 'age': 33}
'''

# Get value by key
print(user.get("name"))
print(user["name"])

user_name = user.get("name")
user_name = "Bob"
print(user) # {'name': 'Haim', 'age': 33}

# change value
user["name"] = "Bob"
user["lastName"] = "Mike" # new key
print(user) # {'name': 'Bob', 'age': 33, 'lastName': 'Mike'}

# update dictionary
user.update({
    'courses':["Python", "WEB", 'C++']
})

print(user)
# {'name': 'Bob', 'age': 33, 'lastName': 'Mike', 'courses': ['Python', 'WEB', 'C++']}

# all dictionary methods 
# 
# change value
user["name"] = "Bob"
user["lastName"] = "Mike"  # new key
print(user)  # {'name': 'Bob', 'age': 33, 'lastName': 'Mike'}

# update dictionary
user.update({"courses": ["Python", "WEB", "C++"]})

print(user)
# {'name': 'Bob', 'age': 33, 'lastName': 'Mike', 'courses': ['Python', 'WEB', 'C++']}

# all dictionary methods
# https://www.w3schools.com/python/python_ref_dictionary.asp

# looping dictionary
"""
{}.keys()
{}.values()
{}.items()
"""

customer = {
    "id": 1,
    "first_name": "Pace",
    "last_name": "Jellyman",
    "email": "pjellyman0@weibo.com",
    "gender": "Male",
    "ip_address": "93.121.209.248",
}

for v in customer.values(): print(f'Next value = {v}')
'''
Next value = 1
Next value = Pace
Next value = Jellyman
Next value = pjellyman0@weibo.com
Next value = Male
Next value = 93.121.209.248
'''
for k in customer.keys(): print(f'Next key = {k}')
'''
Next key = id
Next key = first_name
Next key = last_name
Next key = email
Next key = gender
Next key = ip_address
'''
for pair in customer.items(): 
    print(f'Next pair = {pair}')
    k,v = pair
    print(f'key = {k} val = {v}')
'''
Next pair = ('first_name', 'Pace')
key = first_name val = Pace
Next pair = ('last_name', 'Jellyman')
key = last_name val = Jellyman
Next pair = ('email', 'pjellyman0@weibo.com')
key = email val = pjellyman0@weibo.com
Next pair = ('gender', 'Male')
key = gender val = Male
Next pair = ('ip_address', '93.121.209.248')
key = ip_address val = 93.121.209.248
'''