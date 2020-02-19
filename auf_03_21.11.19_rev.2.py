# Eduard

# eingabe
params = input('Rows + Column bitte eingeben: ')

# convert
params = [x.strip(' ') for x in list(params.split(','))]
row, column = int(params[0]), int(params[1])

# function
def pascal(row, column):
       if column == 0:
           return 1
       elif row == 0:
           return 0
       else:
           return pascal(row-1, column) + pascal(row-1, column-1)

# output
for i in range(0,row):
 print()
 for j in range(0,column):
  if pascal(i, j) != 0:
   print(pascal(i, j), end=' ')
