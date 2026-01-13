from cryptography.fernet import Fernet
import sys
import os
from hashlib import sha256
import hashlib
import base64
from getpass import getpass

def password_to_base64_hash(password: str):
    # 1. Hash SHA256 para obtener 32 bytes
    hash_bytes = hashlib.sha256(password.encode()).digest()
    
    # 2. Codificar a Base64 URL-safe (como Fernet lo requiere)
    clave_fernet = base64.urlsafe_b64encode(hash_bytes)

    return clave_fernet

##COLORS
RED = '\033[91m'
NORMAL = '\033[0m'
##DECRYPTION SCRIPT##

global doAll
doAll = False

try:
    note_name = sys.argv[1]
except:
    doAll = True

password = getpass("Enter encryption password: ")

key = password_to_base64_hash(password)

fernet = Fernet(key)

if doAll:
    for i in os.listdir("notes"):
        with open(f"notes/{i}", "rb") as enc_file:
            encMessage = enc_file.read()
        try:
            decMessage = fernet.decrypt(encMessage).decode()
        except:
            print(f"Note: {i}--> Could not be decrypted with this password.")
            continue
        print(f"Note: {i}--> {decMessage}")

else:
    with open(f"notes/{note_name}.txt", "rb") as enc_file:
        encMessage = enc_file.read()
    try:
        decMessage = fernet.decrypt(encMessage).decode()
    except:
        print(f"{RED}Note: {i}--> Could not be decrypted with this password.{NORMAL}")
    print(decMessage)

input("Press Enter to exit...")
os.system('cls' if os.name == 'nt' else 'clear')







