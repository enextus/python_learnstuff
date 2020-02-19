# Eduard

# input
import math

# endlose Schleife
while True:
    r = input ("Enter the radius of the circle : ")
    try:
        r = float(r)
        break
    except ValueError:
        print("No.. the input string is not a number. It's a string")

# decorator Funktion
def my_decorator(func):
 def wrapper():
  if r < 0:
   print('Falsche Eingabe!')
  else:
   print(func())
 return wrapper

# decoration
@my_decorator
def input_func():
      
# input
 while True:
  try:
   temperatur = input ("Gebe das Temperatur ein. (Float): ")
   temperatur = float(temperatur)
   break
  except ValueError:
       print("No.. the input string is not a number. It's a string")
return area

# start der Funktion
input_func()