# class Hund
class Dog:
    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def set_spitzname(self, spitzname):
     self.spitzname = spitzname


# Test

d = Dog('gaw', 12)

print(d.name)
print(d.age)
d.set_spitzname("Kuzja")
print(d.spitzname)