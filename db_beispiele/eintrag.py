# import sqlite3
# verb=sqlite3.connect("kunden.db")
# c=verb.cursor()

# c.execute(""" INSERT INTO person (name, telefon) VALUES ('Pink Panther', '12345'); """)
# # wichtig: Änderungen speichern
# verb.commit()
# # wichtig: postbote 'cursor' zurück holen und verbindung trennen
# c.close()
# verb.close()


import sqlite3
verb=sqlite3.connect("myimdb.db")
c=verb.cursor()

c.execute(""" INSERT INTO person (name, telefon) VALUES ('Pink Panther', '12345'); """)
# wichtig: Änderungen speichern
verb.commit()
# wichtig: postbote 'cursor' zurück holen und verbindung trennen
c.close()
verb.close()