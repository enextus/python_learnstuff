import math

def our_decorator(func):

    def function_wrapper(x):
        print("Before calling " + func.__name__)
        print(f"002. x: {x}")
        func(x)
        print("After calling " + func.__name__)

    return function_wrapper

@our_decorator
def square_root(x):
    print(f"Hi, the method has been called with argument {str(x)}")
    number = int(x)
    sqrt = math.sqrt(number)
    print(f"square root: {sqrt}")

square_root(4)

# class A:
#     def __init__(self, a, b):
# 	    self.a = a
# 	    self.b = b
# 	    print("An instance of A was initialized")
#     def __call__(self, *args, **kwargs):
        
#         print(args[0]**2 if any(args) else "args - leer" )
#         print(kwargs if any(kwargs) else "kwargs - leer")
