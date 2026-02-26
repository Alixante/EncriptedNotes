import os
import rich
from rich.console import Console 
from rich.table import Table
console = Console()

def getNumber():
    numero = input("Ingresa un número: ")
    
    if numero.isdigit():  # Solo dígitos (0-9)
        return int(numero)
    else:
        return -1
        
def waitForInput():
    input()

def printMenu():
    console.print(
'''
┌────────────┤ ENCRYPTED NOTES ├────────────┐
│                                           │
│    1 -- New                               │
│    2 -- Decrypt                           │
│    3 -- Edit                              │
│    4 -- Config                            │
│    5 -- Exit                              │
│                                           │
└───────────────────────────────────────────┘
''')
    
def printHeader(title: str):
    rich.print(
f"""
────────────┤ {title} ├────────────
"""
    )



def printConfigMenu():
    console = Console()
    table = Table(title="Default configs")
    table.add_column("Index", style="white", justify="center")
    table.add_column("Config", style="green", justify="left")

    table.add_row("1", "Change Default Password")
    table.add_row("2", "Default Privacy Mode")

    console.print(table)