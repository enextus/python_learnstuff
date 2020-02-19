import sqlite3
# DB anlegen
connection = sqlite3.connect("lagerverwaltung.db")
# cursor-object
cursor = connection.cursor()
# tabellen anlegen

try: 

    cursor.execute(""" INSERT INTO lager(1, 2345345345, 'Grafikkarte Typ 1a', 'FC', 0); """)

    # änderungen in der DB speichern mit cursor.commit()
    cursor.commit()
except: 
    print('Ein Fehler ist aufgetreten!')
    # rollback
    connection.rollback()

# verbindung trennen
cursor.close()
connection.close()

# Datentypen von SQL(Py): NULL(None), INTEGER(int), REAL(float), TEXT(str), BLOB(bytes)