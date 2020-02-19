
import math

def g():
    print("01. Hi, it's me 'g'")
    print("02. Thanks for calling me")
    
def f(func):
    print("03. Hi, it's me 'f'")
    print("04. I will call " + func.__name__ + " now")

    # func(0)
    print("05. func's real name is " + func.__name__)


print(f"06. g.__name__: {g.__name__}")
print("\n")
g()
print("\n")
f(g)
print("\n")
f(math.sin)