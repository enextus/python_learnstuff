# tuple: inmuttable, geordnete Folge von Daten
# t = (1, 2, 3)
# print(t)
# print(type(t))
# a = sorted(t)
# print(type(a))
# print(a)

# print(t[1])
# u = (1, 2, [3, 4, 5])
# print(u)
# # Achtung! Veränderbare Elemente im tule sind veränderbar
# u[2].pop()
# print(u)

# thistuple = ("apple", "banana", "cherry", "orange")
# print(thistuple)
# print(thistuple[2:5])

# print(id(thistuple))

# t = (1)

a = input("Gib mir eine Zahl: ")
b = input("Gib mir jetzt die zweite Zahl: ")
if a > b:
    a, b = b, a #swap
print('Die grössere Zahl lautet jedenfalls: ', b)
