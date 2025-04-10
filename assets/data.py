itensPossuidos = ["", "", ""]


import os

def limpar_tela():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux ou macOS
        os.system('clear')