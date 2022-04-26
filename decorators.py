'''
import functools

def tracer(func):
    @functools.wraps(func)
    def wrapper():
        print("Entering...")
        func()
        print("Exiting...")
    wrapper.count += 1
    return wrapper, 


@tracer
def hello_world():hey jnpocu
    print('Hello World!')
'''

hello: str = "hello world"

def add(x: int, y:int) -> int:
    return x + y

new_value: int = add(4, 5)

