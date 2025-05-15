itensPossuidos = ["", "", ""]


import os
import time

def limpar_tela():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux ou macOS
        os.system('clear')


def printDigitado(text, tempo):
    for i in text:
        print(i, end='', flush=True)
        time.sleep(tempo)
