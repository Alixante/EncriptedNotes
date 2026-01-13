from cryptography.fernet import Fernet
import sys
import os
from hashlib import sha256
import hashlib
import base64
from getpass import getpass
import colorama

def password_to_base64_hash(password: str):
    # 1. Hash SHA256 para obtener 32 bytes
    hash_bytes = hashlib.sha256(password.encode()).digest()
    
    # 2. Codificar a Base64 URL-safe (como Fernet lo requiere)
    clave_fernet = base64.urlsafe_b64encode(hash_bytes)

    return clave_fernet

##COLORS
colorama.init()
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
            print(colorama.Fore.GREEN, f"Note: {i}--> {decMessage}",colorama.Fore.RESET)
        except:
            print(colorama.Fore.RED,f"Note: {i}--> Could not be decrypted with this password.", colorama.Fore.RESET)
            continue

else:
    with open(f"notes/{note_name}.txt", "rb") as enc_file:
        encMessage = enc_file.read()
    try:
        decMessage = fernet.decrypt(encMessage).decode()
        print(colorama.Fore.GREEN,decMessage,colorama.Fore.RESET)
    except:
        print(colorama.Fore.RED, f"Note: {note_name}--> Could not be decrypted with this password.", colorama.Fore.RESET)

input("Press Enter to exit...")
os.system('cls' if os.name == 'nt' else 'clear')







