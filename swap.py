# input
while True:
    try:
        a = int(input('Gib mir eine Zahl: '))
        break
    except:
        print("Bitte geben Sie eine Zahl ein: ")

while True:
    try:
        b = int(input('Gib mir jetzt die zweite Zahl: '))
        break
    except:
        print("Bitte geben Sie eine Zahl ein: ")

if a > b:
# swap
    a, b = b, a
# print   
print('Die grössere Zahl lautet jedenfalls: ', b)

