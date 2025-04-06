from assets.itens import Itens
from player.status import Char

import time
import os


def ferreiro():
  Char.where = "Ferreiro"
  from player.inventario import inventory
  from assets.data import itensPossuidos
  from resources.menu import menu
  from resources.venderArma import venderArma

  print("Bem vindo ao ferreiro!")
  os.system('cls')
  print(f"Você tem {Char.moedas} moedas!")
  print("[0] - Voltar")
  print(f"[1] - {Itens.venda[3]} | 5 moedas | +0.5 ATK")
  print(f"[2] - {Itens.venda[4]} | 10 moedas | +1.0 ATK")
  print(f"[3] - {Itens.venda[5]} | 20 moedas | +1.5 ATK")
  option = input("Escolha uma opção: ")

  if not option.isdigit():
    os.system('cls')
    print("Opção inválida!")
    time.sleep(1)
    os.system('cls')
    ferreiro()
  else:
    option = int(option)

  if option == 0:
    os.system('cls')
    print("Saindo do ferreiro...")
    time.sleep(1)
    menu()

  elif option == 1:
    if Char.arma != "":
      os.system('cls')
      print("Você já tem uma arma equipada!")
      option = input("Deseja vender a arma atual? [s/n]: ")
      if option == "s":
        venderArma()
      elif option == "n":
        os.system('cls')
        print("Não é possivel comprar uma arma com outra equipada.")
        time.sleep(1)
        os.system('cls')
        print("Voltando ao menu...")
        time.sleep(1)
        os.system('cls')
        menu()
      else:
        print("Opcão Inválida!")
        time.sleep(1)
        os.system('cls')
        ferreiro()
    elif Char.moedas >= 5:
      Char.arma = "Espada de Madeira"
      Char.atualizar_ataque()
      Char.moedas -= 5
      os.system('cls')
      print(f"Você comprou {Itens.venda[3]}!")
      time.sleep(2)
      menu()

  elif option == 2:
    if Char.arma != "":
      os.system('cls')
      print("Você já tem uma arma equipada!")
      option = input("Deseja vender a arma atual? [s/n]: ")
      if option == "s":
        venderArma()
      elif option == "n":
        os.system('cls')
        print("Não é possivel comprar uma arma com outra equipada.")
        time.sleep(1)
        os.system('cls')
        print("Voltando ao menu...")
        time.sleep(1)
        os.system('cls')
        menu()
      else:
        print("Opcão Inválida!")
        time.sleep(1)
        os.system('cls')
        ferreiro()
      venderArma()
    elif Char.moedas >= 10:
      Char.arma = "Espada de Prata"
      Char.atualizar_ataque()
      Char.moedas -= 10
      os.system('cls')
      print(f"Você comprou {Itens.venda[4]}!")
      time.sleep(2)
      menu()



  elif option == 3:
    if Char.arma != "":
      os.system('cls')
      print("Você já tem uma arma equipada!")
      option = input("Deseja vender a arma atual? [s/n]: ")
      if option == "s":
        venderArma()
      elif option == "n":
        os.system('cls')
        print("Não é possivel comprar uma arma com outra equipada.")
        time.sleep(1)
        os.system('cls')
        print("Voltando ao menu...")
        time.sleep(1)
        os.system('cls')
        menu()
      else:
        print("Opcão Inválida!")
        time.sleep(1)
        os.system('cls')
        ferreiro()
      venderArma()
    elif Char.moedas >= 20:
      Char.arma = "Espada de Ouro"
      Char.atualizar_ataque()
      Char.moedas -= 20
      os.system('cls')
      print(f"Você comprou {Itens.venda[5]}!")
      time.sleep(2)
      menu()


  else:
    os.system('cls')
    print("Opção inválida!")
    time.sleep(2)
    ferreiro()
