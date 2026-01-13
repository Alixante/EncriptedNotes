from cryptography.fernet import Fernet
import sys
import os

##DECRYPTION SCRIPT##

global doAll

doAll = False

try:
    note_name = sys.argv[1]
except:
    doAll = True

with open("key.txt", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

if doAll:
    for i in os.listdir("notes"):
        with open(f"notes/{i}", "rb") as enc_file:
            encMessage = enc_file.read()
        decMessage = fernet.decrypt(encMessage).decode()
        print(f"Note: {i}--> {decMessage}")

else:
    with open(f"notes/{note_name}.txt", "rb") as enc_file:
        encMessage = enc_file.read()
    decMessage = fernet.decrypt(encMessage).decode()
    print(decMessage)

input("Press Enter to exit...")
os.system('cls' if os.name == 'nt' else 'clear')





