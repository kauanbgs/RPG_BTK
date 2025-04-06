from assets.itens import Itens
from player.status import Char

import time
import os

def taverna():
  from player.inventario import inventory
  from assets.data import itensPossuidos
  from resources.menu import menu
  Char.where = "Taverna"
  os.system('cls')
  print(f"Você tem {Char.moedas} moedas, e está na {Char.where}!")
  print("[0] - Voltar")
  print(f"[1] - {Itens.venda[0]} - 5 moedas")
  print(f"[2] - {Itens.venda[1]} - 3 moedas")
  print(f"[3] - {Itens.venda[2]} - 3 moedas")
  option = input("Escolha uma opção: ")

  if not option.isdigit():
    os.system('cls')
    print("Opção inválida!")
    time.sleep(1)
    os.system('cls')
    taverna()
  else:
    option = int(option)

  if option == 0:
    os.system('cls')
    print("Saindo da taverna...")
    time.sleep(1)
    menu()

  elif option == 1:
    if "" not in itensPossuidos:
      os.system('cls')
      print("Você não tem espaço suficiente no inventário!")
      time.sleep(2)
      taverna()
    elif Char.moedas >= 5:
      if itensPossuidos[0] == "":
        itensPossuidos[0] = Itens.venda[0]
      elif itensPossuidos[1] == "":
        itensPossuidos[1] = Itens.venda[0]
      elif itensPossuidos[2] == "":
        itensPossuidos[2] = Itens.venda[0]
      Char.moedas -= 5
      os.system('cls')
      print(f"Você comprou {Itens.venda[0]}!")
      time.sleep(2)
      taverna()
    else:
      os.system('cls')
      print("Você não tem moedas suficientes!")
      time.sleep(2)
      taverna()

  elif option == 2:
    if "" not in itensPossuidos:
      os.system('cls')
      print("Você não tem espaço suficiente no inventário!")
      time.sleep(2)
      taverna()
    elif Char.moedas >= 3:
      if itensPossuidos[0] == "":
        itensPossuidos[0] = Itens.venda[1]
      elif itensPossuidos[1] == "":
        itensPossuidos[1] = Itens.venda[1]
      elif itensPossuidos[2] == "":
        itensPossuidos[2] = Itens.venda[1]
      Char.moedas -= 3
      os.system('cls')
      print(f"Você comprou {Itens.venda[1]}!")
      time.sleep(2)
      taverna()
    else:
      os.system('cls')
      print("Você não tem moedas suficientes!")
      time.sleep(2)
      taverna()

  elif option == 3:
    if "" not in itensPossuidos:
      os.system('cls')
      print("Você não tem espaço suficiente no inventário!")
      time.sleep(2)
      taverna()
    elif Char.moedas >= 3:
      if itensPossuidos[0] == "":
        itensPossuidos[0] = Itens.venda[2]
      elif itensPossuidos[1] == "":
        itensPossuidos[1] = Itens.venda[2]
      elif itensPossuidos[2] == "":
        itensPossuidos[2] = Itens.venda[2]
      Char.moedas -= 3 
      os.system('cls')
      print(f"Você comprou {Itens.venda[2]}!")
      time.sleep(2)
      taverna()
    else:
      os.system('cls')
      print("Você não tem moedas suficientes!")
      time.sleep(2)
      taverna()

  else:
    os.system('cls')
    print("Opção inválida!")
    time.sleep(2)
    taverna()
