# input
input_liste = eval(input("Geben Sie eine Liste ein: "))
input_liste = list(input_liste)
print("Liste: ", input_liste)

ergebnis = []

i=0

while i < len(input_liste):
    if input_liste[i] > 0:
        ergebnis.append(input_liste[i])
    i += 1

print("ergebnis = ", ergebnis)



