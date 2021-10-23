# Lecture Demo
# Doing encryption on a number using a key


def encrypt(pin: str, key: int) -> str:
    encrypted_string = ""
    # for each character in the pin 
    for char in pin:
        # convert the character to an integer
        num = int(char)
        # add the key to the integer and modulo 10 to wrap it
        shifted_num = (num + key) % 10 # 1 - 1 = 0 , 0 % 10 =0
        # convert the new integer to a string and it to the string
        encrypted_string += str(shifted_num)
    return encrypted_string

def decrypt(pin: str, key: int) -> str:
    return encrypt(pin, -key)

if __name__ == "__main__":
    pins = [
        "1234",
        "2464",
        "0345",
        "8442",
    ]
    
    import random
    for pin in pins:
        key = random.randint(1, 9) # Getting a random key
        print("plain pin", pin) 
        encrypted_pin = encrypt(pin, key)
        print("encrypted_pin", encrypted_pin)
        decrypted_pin = decrypt(encrypted_pin, key)
        print("decrypted_pin", decrypted_pin)


