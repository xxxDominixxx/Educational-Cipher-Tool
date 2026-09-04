import os

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

#from tools.terminal import clear_terminal