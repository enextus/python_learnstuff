import numpy as np 
a = np.array( [ [0, 1], [3, 4] ] )
# print(a)
# print(a+1)
# print(a*2)
# print(a*a) # Keine Matrixen multiplikation

"""
[[0 1]
 [2 3]]
[[1 2]
 [3 4]]
[[0 2]
 [4 6]]
[[0 1]
 [4 9]]
 """

print(f"", end="\n")
print(np.eye(2, 2, dtype=int)) # eye() Auge wurfel generator
print(f"", end="\n")
print(f"a = {a}")
print(f"", end="\n")
print(a + np.eye(2, 2, dtype=int)) # dtype: datentyp von Elementen

"""
[[0 1]
 [2 3]]
[[1 2]
 [3 4]]
[[0 2]
 [4 6]]
[[0 1]
 [4 9]]
[[1 0]
 [0 1]]
 """

# # mathematische Funktionen: sin() cos()
# v = np.array([1,10,100])
# print(np.log10(v))