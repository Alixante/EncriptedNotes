from cryptography.fernet import Fernet
import os
##ENCRYPTION SCRIPT##

name = input("Enter note name: ")
message = input("Enter the string to be encrypted: ")


with open("key.txt", "rb") as key_file:
    key = key_file.read()


    
fernet = Fernet(key)

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