languages = {'E':0, 'D':1, 'S':2}
menu_file = ['File', 'Datei', 'Archivo']
menu_neu = ['New', 'Neu', 'Nuevo']
menu_window = ['New Window', 'Neues Fenster', 'Nueva Ventana']
menu_open = ['Open', 'Öffnen', 'Abrir']
menu_save = ['Save', 'Speichern', 'Guardar']
menu_save_as = ['Save as', 'Speichern unter', 'Guardar como']

landeszeichen = ['E', 'D', 'S', 'e', 'd', 's']

while True:
    a = input('Wähle die Ausgangssprache aus (E, D oder S): ')
    if a in landeszeichen:
        break
    else:
        print("bitte nur E, D oder S: ")

while True:
    z = input('Wähle das Zielsprache aus (E, D oder S): ')
    if z in landeszeichen:
        break
    else:
        print("bitte nur E, D oder S: ")

menu_result = list(zip(menu_file, menu_neu, menu_window, menu_open, menu_save, menu_save_as))

print('------------------------------------------------------------')
for elem in  list(menu_result[languages[z]]):
    print(elem)
print('------------------------------------------------------------')