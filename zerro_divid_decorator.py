

def zerro_abfangen(func):
 def wrapTheFunction(a,b):
  if b == 0:
   print("Zerro Division!")
  else:
   func(a,b)
 return wrapTheFunction



@zerro_abfangen
def divid(a,b):
 return a/b



divid(10,2)

divid(10,0)
