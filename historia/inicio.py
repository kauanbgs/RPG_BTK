from player.status import Char
from historia.introducao import introducao
from toknow.manual import manual
from toknow.wiki import wiki
from assets.game_state import comecarTimer
from resources.duelo import duelo

def paginaInicial():
  while True:
    print("[1] - Jogar")
    print("[2] - Manual")
    print("[3] - Wiki")
    option = int(input("Escolha uma opção: "))
    if option not in [1, 2, 3]:
      print("Opção inválida!")
      continue
    elif option == 1:
      comecarTimer()
      introducao()
    elif option == 2:
      manual()
    elif option == 3:
      wiki()
    