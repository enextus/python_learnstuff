class A:
	def __init__(self):
		self.__i=1
		self.j=5
	def display(self):
		print(self.__i,self.j)


class B(A):
		def __init__(self):
			super().__init__()
			self.__i=2
			self.j=7

class C(B):
		def __init__(self):
			super().__init__()
			self.__i=27
			self.j=77

a = A()
print(a)

b = B()
print(b)

c = C()
print(c)

print(a == b == c)
print(1 == 1 == 1)

dir(a)
dir(b)
dir(c)

print(A.mro())
print(B.mro())
print(C.mro())

print(isinstance(a, A))
print(isinstance(a, B))
print(isinstance(a, C))

print(isinstance(b, A))
print(isinstance(b, B))
print(isinstance(b, C))

print(isinstance(c, A))
print(isinstance(c, B))
print(isinstance(c, C))

print(a._A__i)