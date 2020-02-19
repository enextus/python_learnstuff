liste = ['1', '2', 'hi', '3', ]
for elem in liste:
    if elem.isdigit():
        print(elem, ' ist eine Ganzzahl')
    else:
        # continue
        # pass
        # break
        print(elem, ' ist keine Ganzzahl')


# .............

wort = 'python'
for elem in wort:
    if elem.isdigit():
        print(elem, ' ist eine Ganzzahl')
    else:
        # continue
        # pass
        # break
        print(elem, ' ist keine Ganzzahl')

# .............

for elem in wort:
    if elem !='0':
        print(elem)