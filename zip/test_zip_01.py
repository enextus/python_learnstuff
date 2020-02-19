a = {'a':1, 'b':2, 'c':3}
b = {'d':4, 'e':5, 'f':6}
c = {'g':7, 'j':8, 'i':9}

[print(i[0], i[1], i[2]) for i in list(zip(a, b, c))]
