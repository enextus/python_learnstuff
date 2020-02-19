import sqlite3

inp_name=input('Wen sucht Du? ')

verb=sqlite3.connect("kunden.db")
c=verb.cursor()

c.execute(""" SELECT * FROM person WHERE name = ? ; """, (inp_name, ) )
# c.execute(""" SELECT name FROM person WHERE name = ? ; """, (inp_name, ) )
# c.execute(""" SELECT telefon FROM person WHERE name = ? ; """, (inp_name, ) )

for line in c:
    print(line)

c.close()
verb.close()