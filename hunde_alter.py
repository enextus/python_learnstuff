# input

while True:
    x = input ("Gebe das Alter in Jahren ein. (Float): ")
    try:
        val = float(x)
        break
    except ValueError:
        print("No.. the input string is not a number. It's a string")

print("Die Altersingabe:", val)

if val <= 1.0:
    alter = (val * 14) / 1
    print("alter1 = ", alter)
elif val >= 1.0 or val <= 2.0:
    alter = 6 + (      (val * 8) / 1     )     
    print("alter2 = ", alter)
elif val >= 2.0:
    alter = (val - 2 ) + ((val - 2 ) * 5)
    print("alter3 = ", alter)









