# stack.append(5)
import random
from collections import deque
q = deque(['marissa', "antonio", 'Erik'])


q.pop()
q.popleft()

# List Comprehensions
# kurz Schreibweise für Listen

squares = [x**2 for x in range(10)]

print(squares)

mylist=[(x, y) for x in [3,2,1] for y in [3,4,5] if x!=y ]
print(mylist)
vect_1=[-4,-3,1,3,5]
vect_2=[x*2 for x in vect_1]

print()
print(vect_1)
print(vect_2)

from random import randint



[random.randint(a, a*2) for a in range(10)]

[(x, x**2) for x in range(4)]


