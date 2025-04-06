import os
import time

from player.inventario import inventory
from player.status import Char
from player.status import status
from assets.itens import Itens
from areas.taverna import taverna
from areas.areas import areas
from areas.ferreiro import ferreiro


def menu():
  while True:
    os.system('cls')
    print("------------------Eldoria-----------------")
    print("[1] - Inventário")
    print("[2] - Status")
    print("[3] - Taverna")
    print("[4] - Explorar")
    if Char.veioFazenda == True:
      print("[5] - Ferreiro")
    option = input("Escolha uma opção: ")

    if not option.isdigit():
        print("Opção inválida!")
        time.sleep(1)
        continue
    else:
      option = int(option)


    if option not in [1, 2, 3, 4, 5]:
      print("Opção inválida!")
      time.sleep(1)
      continue
    elif option == 1:
      os.system('cls')
      print("Abrindo a mochila...")
      time.sleep(1)
      os.system('cls')
      inventory()
    elif option == 2:
      os.system('cls')
      print("Procurando informações...")
      time.sleep(1)
      os.system('cls')
      status()
    elif option == 3:
      os.system('cls')
      print("Entrando na Taverna...")
      time.sleep(1)
      os.system('cls')
      taverna()
    elif option == 4:
      os.system('cls')
      print("Procurando areas...")
      time.sleep(1)
      os.system('cls')
      areas()
    elif option == 5:
      os.system('cls')
      print("Procurando o ferreiro...")
      time.sleep(1)
      os.system('cls')
      ferreiro()