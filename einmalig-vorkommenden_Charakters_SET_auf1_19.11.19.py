# Eduard
# Anzahl einmalig-vorkommenden Charakters in der Eingabe

# input
eingabe = input('Gib bitte ein Wort ein: ')

# unic_chars_in_word_analyse
def unic_chars_in_word_analyse(x):
 print("list(x): ", list(x))
 myset = set(list(x)) # überflüssigen Charakters werden entfdernt
 print("list(myset): ", list(myset))
 print("myset: ", myset)

 return print(eingabe, " enthält ", len(myset), "einmalig-vorkommenden Charakter.")

# ausgabe
unic_chars_in_word_analyse(eingabe)