# from mytest import myname
# print(myname)

# A string, define which mode you want to open the file in:

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exist

# In addition you can specify if the file should be handled as binary or text mode

# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

f = open('demofile.txt', "r")
print(f.read(500))
# print(f.readline())
# print(f.readline(3))

for w in f.read(500):
 if w == "feierabend":
  print('schönen', w)


# sobald wir fertig sind, schließen wir die Datei
f.close()

# del

import os

