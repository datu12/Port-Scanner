from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
import base64

print("Please Input String here: ")
aUserInput = input()

def decrypString(encrypStrinGz):
    pass_phrase = b'667912' #For the pre-foothold switch the pass_phrase to = N3st22
    salt_value = b'1313Rf99' ##For the pre-foothold switch the salt_value to = 88552299
    password_iterations = 3 #For the pre-foothold switch to 2
    init_vector = b'1L1SA61493DRV53Z'  #For the pre-foothold switch the init_vector to = 464R5DFA5DL6LE28
    key_size = 256

    key = PBKDF2(pass_phrase, salt_value, dkLen=key_size//8, count=password_iterations)
    cipher = AES.new(key, AES.MODE_CBC, init_vector)
    
    encrypted_bytes = base64.b64decode(encrypStrinGz)
    decrypted_bytes = cipher.decrypt(encrypted_bytes)
    decrypted_string = decrypted_bytes.rstrip(b'\0').decode('ascii')

    return decrypted_string

# Example usage:

decrypts = decrypString(aUserInput)
print("Decrypted String:", decrypts)
