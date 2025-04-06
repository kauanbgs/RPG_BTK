import time
import os

from player.status import Char
from resources.menu import menu
from areas.areas import areas


def bosqueTerrivel():
  Char.veioNoBosque = True
  from areas.bosque_terrivel2 import bosqueTerrivel2
  from minigames.adivinhacao import jogo_adivinhacao
  from minigames.aposta_dados import apostaDados
  from minigames.roleta import roleta
  from minigames.anagrama import anagrama
  from minigames.reflexo import jogoReflexo
  print("Meu deus! Aton decidiu ir para o bosque terrível! Talvez essa não tenha sido a melhor das suas decisões...")
  time.sleep(3)
  print("O guerreiro sai em sua caminhada, após 3h de uma extensa caminhada, ele escuta um... latido?")
  time.sleep(4)
  print("CRISTO! O bosque terrivel é, na verdade, uma cidade linda com minijogos para ganhar dinheiro! Quem imaginaria?")
  time.sleep(4)
  Char.where = "Bosque Terrível"
  print(f"Você está em {Char.where}.")
  print("[0] - Voltar")
  print("[1] - Jogo da Adivinhação")
  print("[2] - Aposta de Dados")
  print("[3] - Roleta")
  print("[4] - Anagrama")
  print("[5] - Jogo do Reflexo")
  option = int(input("Escolha uma opção: "))
  if option == 0:
    print("Você decidiu voltar para a cidade!")
    time.sleep(2)
    os.system('cls')
    Char.where = "Eldoria"
    areas()
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


  