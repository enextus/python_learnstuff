#https://www.tutorialspoint.com/python3/python_gui_programming.htm # gui-module für python

from tkinter import *
from tkinter import messagebox
from db import Database

db=Database('shop.db')

# methoden:
def populate_list():
  komponent_list.delete(0, END) # http://effbot.org/tkinterbook/listbox.htm # zum Listbox()
  for row in db.fetch():
      komponent_list.insert(END, row)

def add_item():
  if komponent_text.get()=='' or kunde_text.get()=='' or lieferant_text.get()=='' or preis_text.get()=='':
      messagebox.showinfo('Fehler!', 'Bitte alle Felder befüllen!')
      return
  db.insert(komponent_text.get(), kunde_text.get(), lieferant_text.get(), preis_text.get())
  komponent_list.delete(0, END)
  komponent_list.insert(END, (komponent_text.get(), kunde_text.get(), lieferant_text.get(), preis_text.get()))
  clear_item()
  populate_list()

def select_item(event): 
  ''' hier wird anhand eines 'Events' das zu löschende Element ausgewählt. Muss allerdings eine Bindung vorhin hersgestellt werden - Methode bind()'''
  # print('select')
  try:
    global selected_item
    index=komponent_list.curselection()[0] # Listbox: https://www.tutorialspoint.com/python/tk_listbox.htm  
    selected_item=komponent_list.get(index)
    # print(selected_item)
    # Send the selected item in textfields and delete it
    komponent_eingabe.delete(0, END)
    komponent_eingabe.insert(END, selected_item[1])

    kunde_eingabe.delete(0, END)
    kunde_eingabe.insert(END, selected_item[2])

    lieferant_eingabe.delete(0, END)
    lieferant_eingabe.insert(END, selected_item[3])

    preis_eingabe.delete(0, END)
    preis_eingabe.insert(END, selected_item[4])
  except IndexError:
    pass

def remove_item():
  db.remove(selected_item[0])
  populate_list()

def update_item():
  db.update(selected_item[0], komponent_text.get(), kunde_text.get(), lieferant_text.get(), preis_text.get())
  populate_list()

def clear_item():
  komponent_eingabe.delete(0, END)
  kunde_eingabe.delete(0, END)
  lieferant_eingabe.delete(0, END)
  preis_eingabe.delete(0, END)
  

# Tk() Methode: ein Fenster-Obj. bauen
app = Tk()
# Fenstertitel:
app.title('Lagerverwaltung')
# Fensterdimensionen:
app.geometry('500x350')

# Komponente
# String-Variable
komponent_text=StringVar()
# Label
komponent_label=Label(app, text='Komponent', font=('bold',10), pady=20, padx=0)
# An Gitter binden
komponent_label.grid(row=0, column=0)
# Eingabefeld: Entry()
komponent_eingabe=Entry(app, text=komponent_text)
# Eingabefeld an Gitter binden
komponent_eingabe.grid(row=0, column=1)

# Kunde
# String-Variable
kunde_text=StringVar()
# Label
kunde_label=Label(app, text='Kunde', font=('bold',10))
# An Gitter binden
kunde_label.grid(row=0, column=2)
# Eingabefeld: Entry()
kunde_eingabe=Entry(app, text=kunde_text)
# Eingabefeld an Gitter binden
kunde_eingabe.grid(row=0, column=3)


# Lieferant
# String-Variable
lieferant_text=StringVar()
# Label
lieferant_label=Label(app, text='Lieferant', font=('bold',10))
# An Gitter binden
lieferant_label.grid(row=1, column=0)
# Eingabefeld: Entry()
lieferant_eingabe=Entry(app, text=lieferant_text)
# Eingabefeld an Gitter binden
lieferant_eingabe.grid(row=1, column=1)

# Preis
# String-Variable
preis_text=StringVar()
# Label
preis_label=Label(app, text='Preis', font=('bold',10))
# An Gitter binden
preis_label.grid(row=1, column=2)
# Eingabefeld: Entry()
preis_eingabe=Entry(app, text=preis_text)
# Eingabefeld an Gitter binden
preis_eingabe.grid(row=1, column=3)

# warenverzeichnis (Listbox):
komponent_list=Listbox(app, height=10, width=45, border=0)
komponent_list.grid(row=3, column=0, columnspan=3, rowspan=6,pady=20, padx=20)

# scrollbar -- noch ausbaufähig!!
scrollbar=Scrollbar(app)
scrollbar.grid(row=3, column=3) # weil komponent_list columnspan=3
# scrollbar an komponent_list anhängen:
komponent_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=komponent_list.yview)
# Bind select
komponent_list.bind('<<ListboxSelect>>', select_item)

# Buttons
add_btn=Button(app, text='Add New', width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

remove_btn=Button(app, text='Delete', width=12, command=remove_item)
remove_btn.grid(row=2, column=1)

update_btn=Button(app, text='Update', width=12, command=update_item)
update_btn.grid(row=2, column=2)

clear_btn=Button(app, text='Reset', width=12, command=clear_item)
clear_btn.grid(row=2, column=3)

# populate data
populate_list()

# Programm starten:
app.mainloop()

# for windows
# pyinstaller muss für windows vorher installiert werden: pip install pyinstaller
# pyinstaller lager.py --onefile --windowed
# for mac
# pyinstaller --onefile --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' part_manager.py
# '''
