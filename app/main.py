import os
import rich
import datetime
import sys

from rich.console import Console
from rich.table import Table

import utils.options as options
import utils.decrypt as decrypt
import utils.encrypt as encrypt
import utils.menu as menu

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

console = Console()
while(1):
    console.clear()
    cls()
    
    menu.printMenu()
    
    index = menu.getNumber()
    console.clear()
    
    match index:
        case 1:  # New note
            console.clear()
            options.NewOption()

        case 2:  # Decrypt notes
            console.clear()
            options.DecryptOption()

        case 3:  # Edit (not implemented yet)
            console.clear()
            options.EditOption()
            menu.waitForInput()

        case 4:  # Config
            console.clear()
            menu.printConfigMenu()
            menu.waitForInput()

        case 5:
            sys.exit(1)



