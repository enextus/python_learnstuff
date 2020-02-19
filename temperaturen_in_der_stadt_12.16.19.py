# Eduard

cities=[("Berlin", 12), ("Hamburg", 10), ("Düsseldorf", 11), ("Frankfurt", 9)]
def make_c_f_convertation(c):
    f = c*9/5+32
    return f
for i in cities:
    print(f'{i[0]}: {make_c_f_convertation(i[1])}')