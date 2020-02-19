# Eduard

# input
n = int(input('Gib bitte eine ganze Zahl ein: '))

# function
def func_sum(n):
 if n == 0:
  return 0
 return n + func_sum(n - 1)

# output
print("Die Summe der ersten", n, "Zahlen ist", func_sum(n), end=".")