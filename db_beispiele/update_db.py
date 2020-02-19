import sqlite3

verb=sqlite3.connect("kunden.db")
c=verb.cursor()

def print_table(x):
    c.execute(""" SELECT * FROM person ; """)
    for line in c:
        sp = line
        print(sp)
    print(f'{x} - is done')

print_table('ist Zustand')

input_telefon=input('Bei welcher Telefonnummer soll Name geändert werden? ')
input_name=input('Wie input_name? ')

print('start cursor')
print_table("After verbindung")

c.execute(""" UPDATE person SET name=? WHERE telefon=? ; """, (input_name, input_telefon))

verb.commit()

print_table('after an update')
print('the update is done')

c.close()
verb.close()