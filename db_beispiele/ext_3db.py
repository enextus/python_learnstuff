import sqlite3
conn=sqlite3.connect("myimdb.db")
c=conn.cursor()

c.execute("""SELECT movie.id, movie.title, movie.year, director.name FROM movie, director WHERE movie.director_id = director.id; """)

for line in c:
    print(line)
 
c.close()
conn.close()
 
# >>> (1, 'Amadeus', '1984', 'Forman') alle infos in einer Zeile - wie?