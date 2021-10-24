# Create an encrypt function that takes in ain textnd a numeric shift.
# the phrase will then be shifted that many letters.
# E.g. encrypt(‘abc’,1) would return ‘bcd’ = E.g. encrypt(‘abc’, 10) would return ‘klm’
# shifts that exceed 26 should wrap around
# E.g. encrypt(‘abc’,27) would return ‘bcd’
# Source: https://teachen.info/cspp/unit4/lab04-02.html 


def encrypt(message:str, key:int):
    result = ""
    message = message.lower()
    alpha = "abcdefghijklmnopqrstuvwxyz"
    
    
    for letter in message:  
     if letter in alpha: #if the letter is actually a letter #encrypt it
            #find the letter in the alphabet
            #find the corresponding ciphertext letter in the alphabet
            letter_index = (alpha.find(letter) + key)%  len(alpha) #26
            result = result + alpha[letter_index]
     else:
      result = result + letter
    return result

def decrypt(pin: str, key: int) -> str:
    return encrypt(pin, -key)

print(encrypt('abc', 10))

print(decrypt('KLM', 10))