import base64
import hashlib
import re
import os

from hashlib import sha256
from cryptography.fernet import Fernet
from getpass import getpass

import utils.menu as menu

def is_valid_filename_simple(filename):
    """
    Check if filename contains only valid characters
    """
    # Invalid characters across most OS: \ / : * ? " < > |
    invalid_chars = r'[<>:"/\\|?*]'
    
    if re.search(invalid_chars, filename):
        return False
    
    # Check for empty or dot-only names
    if not filename or filename in ('.', '..'):
        return False
    
    # Check length (most filesystems: 255 chars)
    if len(filename) > 255:
        return False
    
    return True

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


def encrypt_note():
    """Interactive helper that asks for password, note name, and message then writes encrypted file."""
    password = getpass("Enter encryption password: ")
    key = password_to_base64_hash(password)
    fernet = Fernet(key)

    

    menu.printHeader("New Note")
    print()
    message = input("")

    print()
    name = input("File name: ")
    ##while(is_valid_filename_simple(name)):
        ##name = input("Enter valid note name: ")

    encMessage = fernet.encrypt(message.encode())
    try:
        with open(f"notes/{name}.txt", "wb") as enc_file:
            enc_file.write(encMessage)
    except:
        print("Could not save file")

    input("Press Enter to exit...")
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    # run as a standalone script
    encrypt_note()
