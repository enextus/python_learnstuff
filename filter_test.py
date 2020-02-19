# temp = [1, 2, 22, 8.5, 122]

# # 1. Lösung

# meanv = sum(temp)/len(temp)
# print(f'meanv: {meanv}')

# # 2. Lösung
# import statistics
# print(f'statistics.mean(temp): {statistics.mean(temp)}')

# # ########################################################

# avg = statistics.mean(temp)

# print('Durchschnitt: ', avg)
# # filter(funktion, array)
# # filter() wendet die funktion 'funktion' auf jedes Element des 'array' an
# # und liefet ein filter-Object zurück
# # filter-Object mit list() in eine Liste umwandeln!

# print(list(filter(lambda x: x < avg, temp)))

cities=["Berlin", "", "Hamburg",  "",  "", {}, "Düsseldorf",  "", "Frankfurt", "", False, [], (), 0.0, 5, 5.0]
# None-Objecte mit dem filter() ausschließen

raw1 = list(filter(lambda x: bool(x), cities))
raw2 = list(filter(lambda x: x, cities))
raw3 = list(filter(None, cities))
print(raw1)
print(raw2)
print(raw3)