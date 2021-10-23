# Lab: 18 - Cryptography
* Cryptography is the study of secure communications techniques that allow only the sender and intended recipient of a message to view its contents.
![](https://cdn.ttgtmedia.com/rms/onlineImages/security_cissp_cryptography_mobile.jpg)


## Encrypt vs. encipher, Decrypt vs. decipher


![](https://media.geeksforgeeks.org/wp-content/uploads/Encryption_vs_Encoding_vs_Hashing_1.png)


## Caesar cipher:
* It is a encryption techniques
* It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.

## Used Libraries:
* nltk (Natural Language Toolkit)[https://www.nltk.org/]
* black

## How to code Caesar cipher:
1. loop through each character and convert it to int
2. add the key to the integer and modulo 10 to wrap it
3. convert the new integer to a string

## How to check is English word
1. `nltk.download('words', quiet=True)`
2. 