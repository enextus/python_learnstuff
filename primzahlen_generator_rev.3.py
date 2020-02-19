# Eduard
# Prinmzahlen Generator via yield 

# Yield funktion für Primzahlen
def primzahlen():
 yield 2
 liste = [2] # Initialisieren die Liste mit der Zahl 2
 n = 3 # Mit 3 beginnend prüfen wir nur ungerade Zahlen

# endlose Schleife
 while True:
    if all(n%i for i in liste): # Wenn n nicht teilbar durch primzahl aus der Liste
        liste.append(n) # ... dann append this digit to the list of prime digit
        yield n

    n += 2

# Yield object
p = primzahlen()

# Ausgabe
for i in range(10):
    print(next(p))
