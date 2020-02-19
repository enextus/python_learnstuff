# Eduard
# fibonacci

# import
import matplotlib.pyplot as plt

# input
while True:
    try:
        x = int(input('Gib mir eine Ganzzahl ein: '))
        break
    except:
        print("Bitte geben Sie eine Zahl ein: ")

# anfangsparameters for fib liste
fibbonacci_folge = [0,1] 
next_element = 1

# anfangsparameters for loop
i = 1
sequence_number = [0, 1]

# fib function M[n] = fib(n - 1) + fib(n - 2)
def fib_function(x):
  x.append(x[-1]+x[-2])
  return x

# loop
while i <= x:
  fib_function(fibbonacci_folge)
  i = i + 1
  sequence_number.append(i)

# output
print('fibbonacci_folge:', fibbonacci_folge)
print('sequence_number: ', sequence_number)

# format constants
SMALL_SIZE = 7
MEDIUM_SIZE = 10
BIGGER_SIZE = 12

# format functions
def format_function(a, b, c, fibbonacci_folge, sequence_number):
 # params
 plt.rc('font', size=a)          # controls default text sizes
 plt.rc('axes', titlesize=a)     # fontsize of the axes title
 plt.rc('axes', labelsize=b)    # fontsize of the x and y labels
 plt.rc('xtick', labelsize=a)    # fontsize of the tick labels
 plt.rc('ytick', labelsize=a)    # fontsize of the tick labels
 plt.rc('legend', fontsize=a)    # legend fontsize
 plt.rc('figure', titlesize=c)  # fontsize of the figure title
 # render
 plt.bar(sequence_number, fibbonacci_folge)
 plt.suptitle('fibonacci Folge-Entwicklung')
 plt.show()

# format output
format_function(SMALL_SIZE, MEDIUM_SIZE, BIGGER_SIZE, fibbonacci_folge, sequence_number)

