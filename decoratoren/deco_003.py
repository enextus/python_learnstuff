# decorator func

def d_f(func):
    
    def function_wrapper(x):
        print("\nBefore calling " + func.__name__)
        print(f"\n002. x: {x}")
        func(x)
        print("\nAfter calling " + func.__name__)

    return function_wrapper


@d_f
def function(x):
    print(f"\nHier: {x}")

function(20)

