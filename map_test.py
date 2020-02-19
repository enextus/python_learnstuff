cities=[("Berlin", 12), ("Hamburg", 10), ("Düsseldorf", 11), ("Frankfurt", 9)]

convert = lambda x: (x[0], x[1] * 1.8 + 32)
raw = map(convert, cities)
liste = list(raw)

print(f'Original list: {cities}')
print(f'Converted list: {liste}')

