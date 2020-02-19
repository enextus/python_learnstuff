import numpy as np

# Auf. 1
v=np.arange(10)
print(f'array "v": {v}')
print(f'array "Dimension": {v.ndim}\n')

# Auf. 2
u3 = np.asarray(list(filter(lambda x : x%2, v)))
print(f'array "2. Ungerade Zahlen": {u3}\n')

# Auf. 3
um = np.flip(v)
print(f'array "Umgekehrtes Array": {um}\n')

# Auf. 4
a = np.array([1,2,3,4,5])
print(f'a: {a}')
b = a[1:4]
print(f'b: {b}') # b: [2 3 4]
print(f'a: {a}')
print(f'b[0]: {b[0]}')
print(f'a: {a}')
b[0] = 200
print(f'a: {a}')
print(f'a[1]: {a[1]}') # a[1]: 200
print(f'a: {a}\n')

# b -> Verweis auf das Sektor (b = a[1:4] )von dem Array a.

# Auf. 5
m = np.arange(4).reshape(2,2)
print(f'm: {m}')
print(f'array "Dimension": {m.ndim}\n')

# Auf. 6
m1 = np.flip(m, 1)
print(f'm1: {m1}\n')

# Auf. 7
print(f'm: {m}')
m2 = np.flip(m, 0)
print(f'm2: {m2}\n')

# Auf. 8
print(f'm: {m}')
m3 = np.flip(m)
print(f'm3: {m3}\n')

# Auf. 9
m4 = m
print(f'm4: {m4}')

m5 = np.delete(m4, 0, 0)
m6 = np.delete(m4, 0, 1)

print(f'm5: {m5}')
print(f'm6: {m6}')

# Auf. 10

array = np.arange(0, 8)                 # 0
array.reshape(2,4)                      # 1
ar = array.reshape(4,2)                 # 2
ar2 = np.delete(ar, np.s_[2:4:], 0)     # 3
ar3 = ar2.flatten()                     # 4
function_to_apply = lambda x : x * x    # 5
list(map(function_to_apply, ar2))


function_to_apply = lambda x : x + 1    # 6
list(map(function_to_apply, ar2))


a = np.array(list(map(function_to_apply, ar2))).reshape(4,4)
aa = np.array( [a,a,a,a])

# np.tile(array, (4, 1))  kacheln 
