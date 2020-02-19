import sqlite3
# DB anlegen
connection = sqlite3.connect("lagerverwaltung.db")
try: 
    with connection:
        cursor = connection.cursor()
        werte = (
            (10, 1145345345, "Grafikkarte Typ 1a", "1FC", 10),
            (20, 2245345345, "Grafikkarte Typ 2a", "2FC", 20),
            (30, 3345345345, "Grafikkarte Typ 3a", "3FC", 30),
        )
        cursor.executemany("insert into lager values (?, ?, ?, ?, ?);", werte)
except sqlite3.DatabaseError as err: 
    print('Ein Fehler ist aufgetreten! Error: ', err)
else:
    print('Eingabe erfolgreich!')
# verbindung trennen
cursor.close()
connection.close()