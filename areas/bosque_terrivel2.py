import time
import os

from player.status import Char
from resources.menu import menu

def bosqueTerrivel2():
  from minigames.adivinhacao import jogo_adivinhacao
  from minigames.aposta_dados import apostaDados
  from minigames.roleta import roleta
  from minigames.anagrama import anagrama
  from minigames.reflexo import jogoReflexo
  Char.where = "Bosque Terrível"
  print(f"Você está em {Char.where}, e tem {Char.moedas} Moedas!")
  print("[0] - Voltar")
  print("[1] - Jogo da Adivinhação - Min 5 Moedas")
  print("[2] - Aposta de Dados - Min 1 Moeda")
  print("[3] - Roleta - Min 2 Moedas")
  print("[4] - Anagrama - Min 3 Moedas")
  print("[5] - Jogo do Reflexo - Min 5 Moedas")
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
  elif option == 4:
    anagrama()
  elif option == 5:
    jogoReflexo()
  else:
    print("Opção inválida! Tente novamente.")
    time.sleep(2)
    os.system('cls')
    bosqueTerrivel2()