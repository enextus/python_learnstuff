s = "global"

def f(x):
 print("1 = ", id(x))
 s = "local"
 print("2 = ", id(s))
 return x


print("3 = ", id(s))
f(s)
print("4 = ", id(s))


