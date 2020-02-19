l1 = ["foo", "baar", "baaaz"]

# Länge des größen Eintrags.
m = max(len(i) for i in l1 + l2)

# Listen formatiert ausgeben
for l in (l1):
    print(" ".join("{0:{1}}".format(i, m) for i in l)) 