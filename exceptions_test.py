# seed
array = [1+3j, 1, 0, -5, True, False, 'chr']

# testen
for a in array:
    if type(a) not in [int, float]:
        # print('a = ', a, ' -> Type Error!')
        raise TypeError('Type Error!')
    else:
        if a < 0:
            # print('a = ', a, ' -> Value Error!')
            raise ValueError('Value Error!')
