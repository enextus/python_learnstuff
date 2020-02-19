import sqlite3
verb=sqlite3
verb=sqlite3.connect("kunden.db")
c=verb.cursor()
c.execute(""" SELECT * FROM person ; """)

for line in c:
    print(line)

c.close()
verb.close()

