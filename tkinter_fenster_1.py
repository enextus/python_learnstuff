from tkinter import *
def gruessen(): # Funktion OHNE return Anweisung am Ende heißt procedure 
    label.config(text='Guten Tag!')
# fenster
fenster = Tk()
# fenster label
label=Label(master=fenster, text='Begrüßung')
# eingebaute Layout-Manager 'packer' - Pack baut das neue Widget in Fensterein:
label.pack()
# Button-Widgets: Button()
button=Button(master=fenster, text='sag Hallo!', command=gruessen)
button.pack()
# 2 gui starten
fenster.mainloop()