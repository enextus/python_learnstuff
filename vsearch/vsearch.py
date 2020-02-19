def search4vowels(phrase:str) ->set:
 """ This function returns any vowels in phrase """
 vowels=set('aeiouAEIOU')
 return vowels.intersection(set(phrase))

def search4letters(phrase:str, letters:str) ->set:
 """ This function returns any letters found in phrase """
 return set(letters).intersection(set(phrase))
