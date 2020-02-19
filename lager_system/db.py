import sqlite3
class Database:
  def __init__(self, db):
    self.conn=sqlite3.connect(db)
    self.cur=self.conn.cursor()
    self.cur.execute("CREATE TABLE IF NOT EXISTS komponente (id INTEGER PRIMARY KEY, komponent TEXT, kunde TEXT, lieferant TEXT, preis REAL)")
    self.conn.commit()
  
  def fetch(self):
    self.cur.execute("SELECT * FROM komponente")
    rows=self.cur.fetchall()
    return rows
  
  def insert(self, komponent, kunde, lieferant, preis):
    self.cur.execute("INSERT INTO komponente VALUES(NULL, ?, ?, ?, ?)",(komponent, kunde, lieferant, preis))
    self.conn.commit()

  def remove(self, id):
    self.cur.execute("DELETE FROM komponente WHERE id=?", (id,))
    self.conn.commit()

  def update(self, id, komponent, kunde, lieferant, preis):
    self.cur.execute("UPDATE komponente SET komponent=?, kunde=?, lieferant=?, preis=? WHERE id=?", (komponent, kunde, lieferant, preis, id))
    self.conn.commit()
  
  def __del__(self):
    print("Verbindung getrennt!")
    self.cur.close() 
    self.conn.close()

# magic methods
# __init__(self) Konstruktor: baut ein Objekt auf.
# __str__(self) inoffizielle Darstellung von Objekt
# __repr__(self) offizielle Darstellung von Objekt
# __del__(self) Dekonstruktor: baut ein Objekt ab.

if __name__=='__main__':
  db=Database('shop.db')
  
  #db.insert("4GB DDR4 Ram", "Heinz Müller", "Microcenter", "160")
  # db.insert("Asus Mobo", "Harry Potter", "Microcenter", "360")
  # db.insert("500w PSU", "Karen Meyer", "Newegg", "80")
  # db.insert("2GB DDR4 Ram", "Julian Reipke", "Newegg", "70")
  # db.insert("24 inch Samsung Monitor", "Monsieur Niemand", "Best Buy", "180")
  # db.insert("NVIDIA RTX 2080", "Albert Einstein", "Newegg", "679")
  # db.insert("600w Corsair PSU", "John F. Kennedy", "Newegg", "130")
  # db.insert("600w Corsair PSU", "John F. Kennedy", "Newegg", "130")
  # db.insert("IBM i9 8 Core Type a9 Processor", "McMillan", "Newegg", "530")
  # print("Eingabe erfolgreich!")