# user inputs
inp_name=input("Wie heißt Du?")
inp_tel=input("Wie lautet deine Telefonnummer?")

# Eintragung in die DB
import sqlite3
verb=sqlite3.connect("kunden.db")
c=verb.cursor()
c.execute(""" INSERT INTO person (name, telefon) VALUES (?, ?); """, 
(inp_name, inp_tel))

verb.commit()
c.close()
verb.close()

