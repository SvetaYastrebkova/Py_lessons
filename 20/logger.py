from datetime import datetime


def my_log(func):
    LOG_TEMPLATE = """
    Function {func_name} called:
    {timestamp}
    Arguments: 
    - args: {args}
    - kwargs: {kwargs}
    Execution time: {execution_time}
    """
    def wrap(*args, **kwargs):
        start = datetime.now() #before        
        result = func(*args, **kwargs)        
        end = datetime.now() #after
        execution_time = (end - start).total_seconds()        
        log = LOG_TEMPLATE.format(
            func_name = func.__name__,
            timestamp = start.strftime("%Y-%m-%d %H:%M:%S"),
            args = args,
            kwargs = kwargs,
            execution_time = f'{execution_time*1000} ms'
        )
        print(log)        
        return result
    return wrap

@my_log
def f1(a,b,c = 100):
    pass

@my_log
def f2(a,b):
    pass


@my_log
def f3():
    pass

f1(1,2,c = 2)
f2(4,3)
f3()

'''
# keyboard control
import keyboard

# print(keyboard.read_event().event_type)
# check if pressed SHIFT, CAPSLOCK , ....

def handler_creator(code):
    valid_keys = {
        'space': 57,
        'del': 83,
    }
    
    def wrapper():        
        print(f'Key {code} clicked')
        pass
    return wrapper

space_handler = handler_creator(87)

while True:
    evnt = keyboard.read_event()
    if evnt.event_type == keyboard.KEY_UP:
        print(evnt.scan_code)
        print(evnt.name)
        print(evnt.time)
        if evnt.name == 'esc': break
        


while True:
    evnt = keyboard.read_event()

    match keyboard.read_event().event_type:
        case keyboard.KEY_UP if evnt.scan_code == 57:
            space_handler()
            pass
    
'''