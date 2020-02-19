# Eduard
# fibonacci

# import
#import matplotlib.pyplot as plt
from bashplotlib.scatterplot import plot_scatter

# input
while True:
    try:
        nterms = int(input('Gib mir eine Ganzzahl ein: '))
        break
    except:
        print("Bitte geben Sie eine Zahl ein: ")

# anfangsparameters for fib liste
fibbonacci_folge = [] 
i = 1
sequence_number = []

# fib function
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

# loop 
for i in range(nterms):
    fibbonacci_folge.append(recur_fibo(i))
    print(recur_fibo(i))
    sequence_number.append(i)
    i = i + 1

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

