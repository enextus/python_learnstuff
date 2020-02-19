def func_append(x):
    y = 'append'
    x.append(y)
    return x

x = ['first_001']
print('x = ', x, '; id = ', id(x), '; type = ', type(x))
print('_______________________________________________________________________')

func_append(x)

print('x = ', x, '; id = ', id(x), '; type = ', type(x))
print('x = ', x, '; id = ', id(x), '; type = ', type(x))