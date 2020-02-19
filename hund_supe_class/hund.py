# class Hund
class Dog:
    # Initializer / Instance Attributes
    def __init__(self, name, age, spitzname=''):
        self.name = name
        self.age = age
        self.spitzname = spitzname
    def set_spitzname(self, spitzname):
     self.spitzname = spitzname


# Test
if __name__ == "__main__":
    d = Dog('gaw', 12)
    print(d.name)
    print(d.age)
    d.set_spitzname("Kuzja")
    print(d.spitzname)