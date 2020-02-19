# Eduard
# Reihe Generator via yield

# yield Funktion
def my_magic_range():
 liste = [1] # Initialisieren die Liste mit der Zahl 1
 n = 1 # Mit 1 beginnend prüfen wir nur ungerade Zahlen

# endlose schleife
 while True: 
  if n % 2 == 0:
   liste.append(-n)
  else:
   liste.append(n)
   
  yield liste[-1]
  n += 1

# yield object
p = my_magic_range()

# ausgabe
for i in range(25):
  print(next(p))
