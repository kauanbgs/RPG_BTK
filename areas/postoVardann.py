import time
import os
from areas.areas import areas
from player.status import Char
from resources.menu import menu
from historia.histVardann import patrulhaVardann

def postoVardannIntro():
  Char.veioVardann = True
  os.system('cls')
  print("Após ter se destacado em Winterfell, Aton é convidado para escoltar uma caravana de suprimentos até o posto avançado de Vardann.")
  time.sleep(4)
  print("Vardann é uma ilha montanhosa, isolada e estratégica, porém constantemente ameaçada por bandidos e mercenários...")
  time.sleep(4)
  print("Após uma longa viagem escoltando a caravana, Aton avista o topo das muralhas de Várdann.")
  time.sleep(4)
  print("Soldados exaustos, trilhas perigosas e o som do vento cortando as pedras anunciam a chegada.")
  time.sleep(4)
  print("Um capitão se aproxima e diz: Precisamos de toda ajuda possível por aqui.")
  time.sleep(5)
  os.system('cls') 

def postoVardann():
  while True:
    print("--Posto avançado de Vardann---")
    print("[1] - Patrulhar arredores")
    print("[1] - Trabalhar com os vigias")
    print("[1] - Gerenciar recursos do posto")
    option = input("Escolha: ")

    if option == "1":
      patrulhaVardann()
    elif option == "2":
      #FAZER ALGO AQUI
      areas()
    elif option == "3":
      #FAZER ALGO AQUI
      areas()
