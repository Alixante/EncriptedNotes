import os
import rich
import datetime

from rich.console import Console
from rich.table import Table

from utils.menu import printConfigMenu

NOTES_PATH = os.path.join("notes")

console = Console()

table = Table(title="Notes")
table.add_column("Name", style="cyan", justify="center")
table.add_column("Last modified", style="magenta", justify="center")
table.add_column("Size", style="green", justify="center")

for i in os.listdir(NOTES_PATH):
    filePath = (str)(os.path.join(NOTES_PATH, i))
    modTime = (str)(datetime.datetime.fromtimestamp(os.path.getmtime(filePath)).strftime("%Y-%m-%d %H:%M:%S"))
    sizeFile = (str)(os.path.getsize(filePath))
    table.add_row(i, modTime, sizeFile)

console.print(table)

printConfigMenu()


