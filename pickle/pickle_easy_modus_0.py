import pickle
import sqlite3
from collections import namedtuple

# Simple class representing a record in our database.
MemoRecord = namedtuple("MemoRecord", "key, task")

class DBPickler(pickle.Pickler):

    def persistent_id(self, obj):
        # Instead of pickling MemoRecord as a regular class instance, we emit a
        # persistent ID.
        if isinstance(obj, MemoRecord):
            # Here, our persistent ID is simply a tuple, containing a tag and a
            # key, which refers to a specific record in the database.
            return ("MemoRecord", obj.key)
        else:
            # If obj does not have a persistent ID, return None. This means obj
            # needs to be pickled as usual.
            return None

class DBUnpickler(pickle.Unpickler):

    def __init__(self, file, connection):
        super().__init__(file)
        self.connection = connection

    def persistent_load(self, pid):
        # This method is invoked whenever a persistent ID is encountered.
        # Here, pid is the tuple returned by DBPickler.
        cursor = self.connection.cursor()
        type_tag, key_id = pid
        if type_tag == "MemoRecord":
            # Fetch the referenced record from the database and return it.
            cursor.execute("SELECT * FROM memos WHERE key=?", (str(key_id),))
            key, task = cursor.fetchone()
            return MemoRecord(key, task)
        else:
            # Always raises an error if you cannot return the correct object.
            # Otherwise, the unpickler will think None is the object referenced
            # by the persistent ID.
            raise pickle.UnpicklingError("unsupported persistent object")


# class Input_data:
class Inputdata:
    """
    test Input_data
    """
    # Methode input_variable
    @classmethod
    def input_variable(x):
        return input('Bitte eingabe: ')
    # Methode from_input  
    @classmethod
    def from_input(cls):
        return cls(
                    Inputdata.input_variable(), 
                    Inputdata.input_variable()
                )
    def __del__(self):
        print(f'finalizer for the Class-Inputdata was doned\n')

class A(Inputdata):
    """
    test class
    """
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = {1,2,3}
        self.d = [1,2,3,4]
        self.e = 1,2,3,4
    
    def __del__(self):
        print(f'1. finalizer for the Class-A was doned\n')
    
    def get_vars_values(self):
        return self.a, self.b, self.c, self.d, self.e

def main():

    import io
    import pprint

    data = A.from_input()

    data_list = [data, data, data]


    # Initialize and populate our database.
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE memos(key INTEGER PRIMARY KEY, task)")

    tasks = data_list

    print(f'1a. tasks: {tasks}')
    print(f'1b. type(tasks): {type(tasks)}\n')


    # print(data)
    print(f'1. data: {data}')
    print(f'2. data.__dict__: {data.__dict__}')
    print(f'type(data): {type(data)}\n')

    # print(data_list)
    print(f'1. data_list: {data_list}')
    print(f'type(data): {type(data)}\n')

    with open('data_list.pickle', 'wb') as f:
        pickle.dump(data_list, f)

    with open('data_list.pickle', 'rb') as f:
        data_new = pickle.load(f)

    print(f'data_new: {data_new}')
    print(f'type(data_new): {type(data_new)}\n')

    for i in data_new:
        print(f'i: {i.get_vars_values()}')

if __name__ == "__main__":
    main()
