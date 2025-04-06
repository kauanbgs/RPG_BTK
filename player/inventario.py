from player.status import Char
from assets.itens import Itens
import time
import os



def inventory():
  from resources.menu import menu
  from assets.data import itensPossuidos
  print("[0] - Voltar")

  if itensPossuidos[0] == "":
      print("[1] - NADA")
  else:
      print(f"[1] - {itensPossuidos[0]}")

  if itensPossuidos[1] == "":
      print("[2] - NADA")
  else:
      print(f"[2] - {itensPossuidos[1]}")

  if itensPossuidos[2] == "":
      print("[3] - NADA")
  else:
      print(f"[3] - {itensPossuidos[2]}")
  itemUsar = input("Escolha um item para usar: ")

  if not itemUsar.isdigit():
       os.system('cls')
       print("Opção inválida!")
       time.sleep(1)
       inventory()
  else:
    itemUsar = int(itemUsar)
    if itemUsar == 0:
        os.system('cls')
        print("Fechando a mochila...")
        time.sleep(1)
        menu()
    elif itemUsar == 1:
        if itensPossuidos[0] == "":
            os.system('cls')
            print("Você não possui esse item!")
            time.sleep(1)
            inventory()
        else:
            if itensPossuidos[0] == "Poção de Vida":
                Char.vida += 40
                os.system('cls')
                print("Você usou uma poção de Vida!")
                time.sleep(1)
                itensPossuidos[0] = ""
                inventory()
            elif itensPossuidos[0] == "Poção de Ataque":
                Char.ataque += 0.1        
                os.system('cls')
                print("Você usou uma poção de Ataque!")
                time.sleep(1)
                itensPossuidos[0] = ""
                inventory()
            elif itensPossuidos[0] == "Poção de Defesa":
                Char.defesa += 0.1
                os.system('cls')
                print("Você usou uma poção de Defesa!")
                time.sleep(1)
                itensPossuidos[0] = ""
                inventory()
    elif itemUsar == 2:
        if itensPossuidos[1] == "":
            os.system('cls')
            print("Você não possui esse item!")
            time.sleep(1)
            inventory()
        else:
            if itensPossuidos[1] == "Poção de Vida":
                Char.vida += 40
                os.system('cls')
                print("Você usou uma poção de Vida!")
                time.sleep(1)
                itensPossuidos[1] = ""
                inventory()
            elif itensPossuidos[1] == "Poção de Ataque":
                Char.ataque += 0.1
                os.system('cls')
                print("Você usou uma poção de Ataque!")
                time.sleep(1)
                itensPossuidos[1] = ""
                inventory()
            elif itensPossuidos[1] == "Poção de Defesa":
                Char.defesa += 0.1
                os.system('cls')
                print("Você usou uma poção de Defesa!")
                time.sleep(1)
                itensPossuidos[1] = ""
                inventory()
    elif itemUsar == 3:
        if itensPossuidos[2] == "":
            os.system('cls')
            print("Você não possui esse item!")
            time.sleep(1)
            inventory()
        else:
            if itensPossuidos[2] == "Poção de Vida":
                Char.vida += 40
                os.system('cls')
                print("Você usou uma poção de Vida!")
                time.sleep(1)
                itensPossuidos[2] = ""
                inventory()
            elif itensPossuidos[2] == "Poção de Ataque":
                Char.ataque += 0.1
                os.system('cls')
                print("Você usou uma poção de Ataque!")
                time.sleep(1)
                itensPossuidos[2] = ""
                inventory()
            elif itensPossuidos[2] == "Poção de Defesa":
                Char.defesa += 0.1
                os.system('cls')
                print("Você usou uma poção de Defesa!")
                time.sleep(1)
                itensPossuidos[2] = ""
                inventory()
    else:
        os.system('cls')
        print("Opção inválida!")
        time.sleep(1)
        inventory()
        