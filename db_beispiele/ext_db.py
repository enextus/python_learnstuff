import sqlite3
conn=sqlite3.connect("myimdb.db")
c=conn.cursor()



# c.execute("""SELECT * FROM director WHERE id=1; """)
# for line in c:
#     print(line)

# c.execute("""SELECT * FROM movie WHERE director_id=1; """)'

# for line in c:
#     print(line)
 
c.execute("""SELECT * FROM movie JOIN director; """)

for line in c:
    print(line)
 
c.close()
conn.close()
 
# >>> (1, 'Amadeus', '1984', 'Forman') alle infos in einer Zeile - wie?