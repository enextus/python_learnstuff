# Eduard

# import
import math

# endlose Schleife und das Input der Daten
while True:
    r = input("Enter the radius of the circle : ")
    try:
        r = float(r)
        if r < 0:
            print('Sinnlose Eingabe! Bitte keine negativen Zahlen eingeben.')
            continue
        else:
            break
    except ValueError:
        print("No.. the input string is not a number! Please repeat the input.")
        continue

# decorator Funktion
def my_decorator(func):
 def wrapper(r):
  if r < 0:
   print('Sinnlose Eingabe. Bitte keine negativen Zahlen eingeben!')
  else:
   print(func(r))
 return wrapper

# # decoration
@my_decorator
def area_of_a_circle(r):
 area = math.pi * r * r
 return area

# Ausgabe
# area_of_a_circle(r)
print(area_of_a_circle(r))