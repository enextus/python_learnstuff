def search_letters(phrase:str, letters:str) -> set:
     return set(letters).intersection(set(phrase))

def print_die_login_daten(x:str, y:str):
    print(f'x: {x}, y: {y}')
    return x, y