from cryptography.fernet import Fernet
import sys
import os
from hashlib import sha256
import hashlib
import base64
from getpass import getpass
import colorama


from utils.config import FILE_PATH


def hashString(text: str, salt: str) -> str:
    textHash = hashlib.sha256(text.encode()).hexdigest()
    saltHash = hashlib.sha3_512(text.encode()).hexdigest()
    
    finalHash = hashlib.sha3_512((textHash+saltHash).encode()).hexdigest()
    return finalHash

def password_to_base64_hash(password: str, salt: str = "") -> bytes:
    password = hashString(password, salt)
    hash_bytes = hashlib.sha256(password.encode()).digest()
    
    clave_fernet = base64.urlsafe_b64encode(hash_bytes)

    return clave_fernet

def password_to_base64_hash_deprecated(password: str):
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

def decryptFile(fernet: Fernet, note_name: str):
    print(FILE_PATH)
    try:
        with open(f"notes/{note_name}.txt", "rb") as enc_file:
            encMessage = enc_file.read()
        try:
            decMessage = fernet.decrypt(encMessage).decode()
            print(colorama.Fore.GREEN,decMessage,colorama.Fore.RESET)
        except:
            print(colorama.Fore.RED, f"Note: {note_name}--> Could not be decrypted with this password.", colorama.Fore.RESET)
            return 0
    except NameError:
        print(colorama.Fore.RED, f"Error: {NameError}", colorama.Fore.RESET)


def decryptAllFiles(password: str, fernet: Fernet):
    print(FILE_PATH)
    for i in os.listdir(FILE_PATH):
        with open(f"{FILE_PATH}/{i}", "rb") as enc_file:
            encMessage = enc_file.read()
        try:
            decMessage = fernet.decrypt(encMessage).decode()
            print(colorama.Fore.GREEN, f"Note: {i}--> {decMessage}", colorama.Fore.RESET)
        except:
            print(colorama.Fore.RED, f"Note: {i}--> Could not be decrypted with this password.", colorama.Fore.RESET)
            continue


def interactive_decrypt():
    """Prompt for password and optionally a note name, then perform decryption."""
    doAll = False
    try:
        note_name = sys.argv[1]
    except IndexError:
        doAll = True

    password = getpass("Enter encryption password: ")
    key = password_to_base64_hash(password)
    fernet = Fernet(key)

    if doAll:
        decryptAllFiles(password, fernet)
    else:
        with open(f"notes/{note_name}.txt", "rb") as enc_file:
            encMessage = enc_file.read()
        try:
            decMessage = fernet.decrypt(encMessage).decode()
            print(colorama.Fore.GREEN, decMessage, colorama.Fore.RESET)
        except:
            print(colorama.Fore.RED, f"Note: {note_name}--> Could not be decrypted with this password.", colorama.Fore.RESET)

    input("Press Enter to exit...")
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    interactive_decrypt()

