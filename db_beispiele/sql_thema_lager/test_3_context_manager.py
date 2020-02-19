import sqlite3
# DB anlegen
connection = sqlite3.connect("lagerverwaltung.db")

try: 
    with connection:
        # cursor-object
        cursor = connection.cursor()
        cursor.execute(""" INSERT INTO lager (fachnummer, seriennummer, komponente, lieferant, reserviert) VALUES (1, 2345345345, "Grafikkarte Typ 1a", "FC", 0); """)

        # änderungen in der DB speichern mit cursor.commit()
        # cursor.commit() mit hilfe von 'with' ist nicht mehr notwendig!

except: 
    print('Ein Fehler ist aufgetreten!')

    # rollback():
    # nicht gewünschte Änderungen Rückgängig
    # connection.rollback() # mit Hilfe von context-manager 'with', brauchen wir rollback nicht mehr ;)

# verbindung trennen
cursor.close()
connection.close()

# Datentypen von SQL(Py): NULL(None), INTEGER(int), REAL(float), TEXT(str), BLOB(bytes)