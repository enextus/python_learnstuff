# Eduard

import csv

file = open("datei.csv", "r")
csv_reader = csv.reader(file, delimiter=",")
for row in csv_reader:
   print(row)
file.close()