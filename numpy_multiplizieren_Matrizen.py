import numpy as np

x=np.array([[1,2],[3,4]])
print(f'x: {x}\n')

y=np.array([[5,6], [7,8]])
print(f'y: {y}\n')
print(f'x*y: {x*y}\n')

# !!!! Keine mathematische multiplikation 2 Matrizen
# Die richtige mathematische multiplikation 2 Matrizen:
#A.dot(B) oder np.dot(B)  oder np.dot(A,B)

produkt=x.dot(y)
print(f'produkt: {produkt}\n')