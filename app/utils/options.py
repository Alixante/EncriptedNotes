

from utils.decrypt import interactive_decrypt
from utils.encrypt import encrypt_note
from utils.menu import *

def NewOption():
    # start the encrypt workflow
    encrypt_note()

def EditOption():
    return 0

def DecryptOption():
    # launch the decrypt helper
    interactive_decrypt()
