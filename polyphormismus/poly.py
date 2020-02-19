from itertools import count

class A():

    _ids = count(1)

    def __init__(self, var_=1):
        self.var_ = var_
        self.id = next(self._ids)
    
    def func_poly(self):
        print(f"instance id = {self.id}")
        print(f"var_ = {self.var_}")
        print(f"* self = {self}")
        print(f"* id(self) = {id(self)}")
    
    def __del__(self):
        print(f"{self}; Status: destroyed.")

class B(A):

    def __init__(self, var_=2):
        super().__init__(var_)

    def func_poly(self):
        print(f"** instance id = {self.id}")
        print(f"** var_ = {self.var_}")
        print(f"** self = {self}")
        print(f"** id(self) = {id(self)}")

def main():

    for i in A(), B():
        i.func_poly()

if __name__ == "__main__":
    main()
