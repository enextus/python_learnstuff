import sqlite3
# DB anlegen
connection = sqlite3.connect("lagerverwaltung.db")

try: 
    with connection:
        cursor = connection.cursor()
        # cursor.execute(""" INSERT INTO lager (fachnummer, seriennummer, komponente, lieferant, reserviert) VALUES (1, 2345345345, "Grafikkarte Typ 1a", "FC", 0); """)
        
        # werte = [
        # (1, 2345345345, "Grafikkarte Typ 1a", "FC", 0),
        # (2, 345645345345, "Grafikkarte Typ 1a", "FC", 0),
        # (3, 45634565345, "Grafikkarte Typ 1a", "FC", 0),
        # (4, 6789786895, "Grafikkarte Typ 1a", "FC", 0),
        # ]
        # cursor.execute(""" INSERT INTO lager VALUES (?, ?, ?, ?, ?); """)
        # for element in werte:
        #     cursor.execute("""INSERT INTO lager VALUES (?, ?, ?, ?, ?);""", element)

        werte = (
            (10, 1145345345, "Grafikkarte Typ 1a", "1FC", 10),
            (20, 2245345345, "Grafikkarte Typ 2a", "2FC", 20),
            (30, 3345345345, "Grafikkarte Typ 3a", "3FC", 30),
        )
        cursor.executemany("insert into lager values (?, ?, ?, ?, ?);", werte)

except sqlite3.DatabaseError as err: 
    print('Ein Fehler ist aufgetreten! Error: ', err)

# verbindung trennen
cursor.close()
connection.close()