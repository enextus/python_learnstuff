# Eduard

# die yield funktion
def my_fibonacci_range():
 # anfangsparameter for fib liste
 fibbonacci_folge = []
 sequence_number = []
 i = 1

 # recursive fibonacci function
 def recur_fibo(n):
  if n <= 1:
   return n
  else:
   return(recur_fibo(n-1) + recur_fibo(n-2))

 # endlose Schleife
 while True:
  fibbonacci_folge.append(recur_fibo(i))
  sequence_number.append(i)
  yield fibbonacci_folge[-1]
  i = i + 1

# create a yield object 
p = my_fibonacci_range()

# ausgabe
for i in range(35):
  print(next(p))
