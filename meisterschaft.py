# Eduard

# import
import collections

# input
land = input('Bitte das Land eingeben: ')

# dictionaries
gruppe_a = {"uruguay":7, "mexico":3, "suedafrika":3, "frankfurt":5}
gruppe_b = {"argentinien":7, "suedkorea":3, "griechenland":3, "nigeria":1}
gruppe_c = {"usa":7, "england":5, "slovenia":3, "algeria":4}
gruppe_d = {"germany":6, "ghana":4, "australien":4}

gruppen_ids = {id(gruppe_a):'gruppe_a', id(gruppe_b):'gruppe_b', id(gruppe_c):'gruppe_c', id(gruppe_d):'gruppe_d'}

# collections
gruppen = collections.ChainMap(gruppe_a, gruppe_b, gruppe_c, gruppe_d)

# logic 
if land in list(gruppen):
 for k, v in gruppen.items():
  if k == land:
   print('{} = {}'.format(k, v))
   break
else:
 print("Das land ist nicht in der Gruppen vorhanden")

for i in gruppen.maps:
 if land in i:
  print('Name der Gruppe: ', gruppen_ids[id(i)])


