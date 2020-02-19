# profiling
criteria = ("brand", "model", "year", "color")

liste = []

for x in range(1, len(criteria)):
    ir = input("Gib bitte ein Brand ein: ")
    liste.append(ir)

print(liste)

profile = dict.fromkeys(criteria, "none")

i = 0
while i < len(liste):
    print(i)
    print(liste[i])
    profile[criteria[i+1]] = liste[i]
    i = i + 1  

print(profile)