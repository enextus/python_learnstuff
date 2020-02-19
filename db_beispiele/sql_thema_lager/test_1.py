import sqlite3
# DB anlegen
connection = sqlite3.connect("lagerverwaltung.db")
# cursor-object
cursor = connection.cursor()
# tabellen anlegen
# CREATE TABLE IF NOT EXISTS <table name>
cursor.execute(""" CREATE TABLE IF NOT EXISTS lager(fachnummer INTEGER, seriennummer INTEGER, komponente TEXT, lieferant TEXT, reserviert INTEGER ); """)
cursor.execute(""" CREATE TABLE IF NOT EXISTS lieferant(kurz TEXT, name TEXT, ort TEXT); """)
cursor.execute(""" CREATE TABLE IF NOT EXISTS kunden(kurz TEXT, name TEXT, ort TEXT); """)
# verbindung trennen
cursor.close()
connection.close()


# Datentypen von SQL(Py): NULL(None), INTEGER(int), REAL(float), TEXT(str), BLOB(bytes)
