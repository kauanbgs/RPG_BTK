import time
import os

from player.status import Char
from resources.menu import menu

def bosqueTerrivel2():
  from minigames.adivinhacao import jogo_adivinhacao
  from minigames.aposta_dados import apostaDados
  from minigames.roleta import roleta
  Char.where = "Bosque Terrível"
  print(f"Você está em {Char.where}.")
  print("[0] - Voltar")
  print("[1] - Jogo da Adivinhação")
  print("[2] - Aposta de Dados")
  print("[3] - Roleta")
  option = int(input("Escolha uma opção: "))
  if option == 0:
    print("Você decidiu voltar para a cidade!")
    time.sleep(2)
    Char.where = "Eldoria"
    menu()
  elif option == 1:
    jogo_adivinhacao()
  elif option == 2:
    apostaDados()
  elif option == 3:
    roleta()
  else:
    print("Opção inválida! Tente novamente.")
    time.sleep(2)
    os.system('cls')
    bosqueTerrivel2()


  