import pickle
import sqlite3
from collections import namedtuple

# Simple class representing a record in our database.
MemoRecord = namedtuple("MemoRecord", "key, task")

class DBPickler(pickle.Pickler):
    """
    class DBPickler
    """
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
    """
    class DBUnpickler
    """
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

class A(Inputdata):
    """
    class A
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

    data_list = [data, data, data, data, data, data, data]
    data_list = pickle.dumps(data_list, protocol=0)

    # Initialize and populate our database.
    # conn = sqlite3.connect(":memory:")
    conn = sqlite3.connect("pickle_test.db")

    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS memos(key INTEGER PRIMARY KEY, task TEXT)")

    # for task in data_list:
    cursor.execute("INSERT INTO memos VALUES(NULL, ?)", (data_list,))

    # Fetch the records to be pickled.
    cursor.execute("SELECT * FROM memos")
    memos = [MemoRecord(key, task) for key, task in cursor]

    # Save the records using our custom DBPickler.
    file = io.BytesIO()
    DBPickler(file).dump(memos)

    # print the pickled records.
    print(f'\n')
    print("Pickled records:")
    pprint.pprint(memos)
    print(f'\n')
    # ________________________________________________________________________

    print(f'{data_list} --------------- {type(data_list)}')
    print(f'\n')

    # Update a record, just for good measure.
    # cursor.execute("UPDATE memos SET task='blabla' WHERE key=1")

    # sql = "UPDATE memos SET task = %s WHERE key = %s"
    # val = (memos, 1)

    # cursor.execute(sql, val)

    # Load the records from the pickle data stream.
    file.seek(0)
    memos = DBUnpickler(file, conn).load()

    # print the unpickled records.
    print("Unpickled records:") 
    pprint.pprint(memos)

    for i in memos:
        result = i[1]

    # loads - obj entpacken
    unpacked_obj = pickle.loads(result, fix_imports=True, encoding="ASCII", errors="strict")
    print(f'\n')
    print(f'pickle.loads(): {unpacked_obj}')

    # for obj in unpacked_obj:
    #     print(f'i: {obj.get_vars_values()}')


if __name__ == "__main__":
    main()
