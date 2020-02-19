# Eduard

# import
import collections

# input
a = input()

# vordefinierten lists
gesuchen_characters = []
counter = 0

# collections methods anwenden
count = collections.Counter(a)

# loop
for i in count.items():
 if i[1] == 1:
  gesuchen_characters.append(i[0])
  counter += 1

print(a, "enthält", counter, "einmalig-vorkommenden Charakters", "In diesem Fall sind es:", gesuchen_characters, end=".")




# logic
# dict = { x:a.count(x) for x in [ x for x in list(a) ] }
# print(dict)

# print( list(sorted((collections.Counter(a).elements() ))))