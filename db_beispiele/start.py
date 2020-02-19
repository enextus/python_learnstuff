import sqlite3

verbindung = sqlite3.connect("myimdb.db")
# Built-In 'Cursor' 

meincurs = verbindung.cursor()
# tabelle neu anlegen: 2 Spalten: Name und Telefon

meincurs.execute("CREATE TABLE person(name text, telefon text)")

