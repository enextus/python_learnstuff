import math

def foo(func):
    print("The function " + func.__name__ + " was passed to foo")
    res = 0
    for x in [1, 2, 2.5]:
        res += func(x)
    return res

print(foo(math.sin))
print(foo(math.cos))



# class C:
#     def __init__(self, x):
#         self.x = x
#     def __repr__(self):
#         return f"C({self.x})"
#     def __hash__(self):
#         return hash(self.x)
#     def __eq__(self, other):
#         return (
#             self.__class__ == other.__class__ and
#             self.x == other.x
#         )

# class Foo(object):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def bar(self):
#         pass


# class Foo(object):
#     def __new__(cls, *args, **kwargs):
#         print("Creating Instance")
#         instance = super(Foo, cls).__new__(cls, *args, **kwargs)
#         return instance
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def bar(self):
#         pass
