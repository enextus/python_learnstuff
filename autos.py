# es hangelt es sich dabei um auto_objekte
# dict

# der gemeinsame bauplan
attribute = ['hersteller', 'model', 'baujahr', 'farbe', 'geschwindigkeit']

# der gemeinsammen bauplan (fromkeys()):
auto = {'hersteller': None,
'model': None,
'baujahr': None,
'farbe': None,
'geschwindigkeit': None}

# objectinstanzen
auto_1_liste = ['bmw', '330i', 1990, 'silber', 0]
auto_1 = {'hersteller':'bmw',
'model':'330i',
'baujahr':'1990',
'farbe':'silber',
'geschwindigkeit':0}
auto_2 = {'hersteller':'audi',
'model':'a1',
'baujahr':'2015',
'farbe':'rot'}
auto_3 = {'hersteller':'vw',
'model':'golf',
'baujahr':'1974',
'farbe':'blau'}

# methoden

def appendfunction(d, x, y):
 d[x] = y
 return

def speed(d, n):
 neu = d['geschwindigkeit'] + n
 d['geschwindigkeit'] = neu
 return

# nested dict
allautos = {
'auto_1':{'hersteller':'bmw',
'model':'330i',
'baujahr':'1990',
'farbe':'silber'},
'auto_2':{'hersteller':'audi',
'model':'a1',
'baujahr':'2015',
'farbe':'rot'},
'auto_3':{'hersteller':'vw',
'model':'golf',
'baujahr':'1974',
'farbe':'blau'}
}

