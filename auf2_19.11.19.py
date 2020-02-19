# Eduard
# Caesar Code

# input
text = input('Gib bitte ein Wort ein: ')

# versatz
versatz = 3

# Caesar Code 
def caesar_encrypt(text, versatz): 
    result = ""
  
    # traverse text 
    for i in range(len(text)): 
        char = text[i] 
  
        # uppercase characters 
        if (char.isupper()): 
            result += chr((ord(char) + versatz-65) % 26 + 65) 
  
        # lowercase characters 
        else: 
            result += chr((ord(char) + versatz - 97) % 26 + 97) 

    return result 

print ("Eingabe-Text: " + text)
print ("Versatz: " + str(versatz))
print ("Caesar Code: " + caesar_encrypt(text, versatz)) 
