from cryptography.fernet import Fernet
import base64
import hashlib
from hashlib import sha256
import os
from getpass import getpass

def password_to_base64_hash(password: str):
    # 1. Hash SHA256 para obtener 32 bytes
    hash_bytes = hashlib.sha256(password.encode()).digest()
    
    # 2. Codificar a Base64 URL-safe (como Fernet lo requiere)
    clave_fernet = base64.urlsafe_b64encode(hash_bytes)

    return clave_fernet

##ENCRYPTION SCRIPT##
password = getpass("Enter encryption password: ")

key = password_to_base64_hash(password)
    
fernet = Fernet(key)

name = input("Enter note name: ")
message = input("Enter the string to be encrypted: ")

encMessage = fernet.encrypt(message.encode())

with open(f"notes/{name}.txt", "wb") as enc_file:
    enc_file.write(encMessage)
# decrypt the encrypted string with the 
# Fernet instance of the key,
# that was used for encrypting the string
# encoded byte string is returned by decrypt method,
# so decode it to string with decode methods
decMessage = fernet.decrypt(encMessage).decode()

input("Press Enter to exit...")
os.system('cls' if os.name == 'nt' else 'clear')