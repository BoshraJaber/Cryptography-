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

print(encrypt('zzz',1)) 

# create a crack function that will decode the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.
# Devise a method for the computer to determine if code was broken with minimal human guidance.

import re
from corpus_loader import word_list, name_list


def crack(message):
    result = ''
    for key in range(0,26):
        decrypt_message = decrypt(message, key)
        candidate_words = decrypt_message.split()
        word_count = 0
        for candidate in candidate_words:
          word = re.sub(r'[^A-Za-z]+','', candidate)
          if word.lower() in word_list or word in name_list:
            # print("english word", word)
             word_count += 1

        percentage = int(word_count / len(candidate_words) * 100)
        if(percentage> 90):
         print(candidate_words)
         result = candidate_words
         
    return result


        
message = encrypt("does it work?", 10)
print('hereeeeee',crack(message))
