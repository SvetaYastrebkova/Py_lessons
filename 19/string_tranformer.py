''''
def string_tranformer(string, worker_function, field_length, spacer): return new_string str.ljust() str.rjust() str.center() string_tranformer('test', str.center) # -> '...test...'
'''

def string_tranformer(string, worker_function, field_length, spacer=" "):
    # worker_function — это метод типа str.ljust / str.rjust / str.center
    new_string = worker_function(string, field_length, spacer)
    return new_string


print(string_tranformer("test", str.ljust, 10, "."))   # 'test......'
print(string_tranformer("test", str.rjust, 10, "."))   # '......test'
print(string_tranformer("test", str.center, 10, "."))  # '...test...'
