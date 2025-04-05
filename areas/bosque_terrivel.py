import time
import os

from player.status import Char
from resources.menu import menu

def bosqueTerrivel():
  from minigames.adivinhacao import jogo_adivinhacao
  print("Meu deus! Aton decidiu ir para o bosque terrível! Talvez essa não tenha sido a melhor das suas decisões...")
  time.sleep(3)
  print("O guerreiro sai em sua caminhada, após 3h de uma extensa caminhada, ele escuta um... latido?")
  time.sleep(4)
  print("CRISTO! O bosque terrivel é, na verdade, uma cidade linda com minijogos para ganhar dinheiro! Quem imaginaria?")
  time.sleep(4)
  print("[0] - Voltar")
  print("[1] - Jogo da Adivinhação")
  print("[2] - Aposta de Dados")
  print("[2] - Descubra a Senha")
  option = int(input("Escolha uma opção: "))
  if option == 0:
    print("Você decidiu voltar para a cidade!")
    time.sleep(2)
    Char.where = "Eldoria"
    menu()
  elif option == 1:
    jogo_adivinhacao()


  