import sqlite3
connection = sqlite3.connect("lagerverwaltung.db")
try: 
    with connection:
        cursor = connection.cursor()
        cursor.execute("select * from lager;")

    # for line in cursor:
    #     print(line)

    # print()
    # print(dir(cursor))

    # # 'fetchall', 'fetchmany', 'fetchone'

    # print() 
    # fa = cursor.fetchall()

    # for line in fa:
    #     print(line)

    # print()
    # fm = cursor.fetchmany()

    # for line in fm:
    #     print(line)
    # print()

    fo = cursor.fetchone()
    print(fo)

except sqlite3.DatabaseError as err: 
    print('Ein Fehler ist aufgetreten! Error: ', err)
else:
    print('Eingabe erfolgreich!')
# verbindung trennen
cursor.close()
connection.close()