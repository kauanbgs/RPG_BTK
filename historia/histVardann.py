import time
import os
from player.status import Char
from resources.d20 import d20
from areas.areas import areas
from assets.data import limpar_tela
from resources.duelo import duelo

def patrulhaVardann():
  from areas.postoVardann import postoVardann

  fezAlgo = False
  if fezAlgo == True:
    print("Você já patrulhou em vardann!")
    postoVardann()
  limpar_tela()
  print("Aton pega sua capa e parte para as trilhas ao redor de Várdann.")
  time.sleep(3)
  print("Durante a patrulha, encontra pegadas e restos de uma fogueira...")
  time.sleep(3)
  escolhaPatrulhaVardann()
def escolhaPatrulhaVardann():
  from areas.postoVardann import postoVardann
  print("[1] - Investigar os rastros")
  print("[2] - Relatar aos guardas")
  option = input("Escolha: ")

  if option == "1":
      limpar_tela()
      print("Aton decide investigar as pegadas, e as segue.")
      time.sleep(2)
      print("Após minutos procurando, Aton encontra um anão (que tem os pés gigantes).")
      time.sleep(2)
      print("O anão é estressado e extremamente forte, ele decide iniciar um duelo.")
      time.sleep(3)
      limpar_tela()
      print("Um duelo foi iniciado!")
      time.sleep(2)
      limpar_tela()
      fezAlgo = True
      duelo("Gnomo", 55, 2.0)
      limpar_tela()
      print("Parábens! Aton venceu o duelo e pode contar aos guardas o que aconteceu. Você ganhou 6 moedas e honra!")
      Char.honra += 1
      Char.moedas += 6
      time.sleep(2)
      postoVardann()
  elif option == "2":
    print("Você decidiu relatar o problema aos guardas")
    time.sleep(2)
    print("Ao chegar em um dos guardas, um anão ofensivo e com pés comicamente grandes é visto")
    time.sleep(2)
    print("O anão é estressado e extremamente forte, ele decide iniciar um duelo.")
    time.sleep(3)
    limpar_tela()
    print("Um duelo foi iniciado!")
    time.sleep(2)
    limpar_tela()
    duelo("Gnomo", 55, 2.0)
    limpar_tela()
    print("Parábens! Aton venceu o duelo e pode contar aos guardas o acontecido. Você ganhou 6 moedas e honra!")
    Char.honra += 1
    Char.moedas += 6
    time.sleep(2)
    postoVardann()
  else:
    limpar_tela()
    print("Escolha não é valida.")
    time.sleep(2)
    limpar_tela()
    escolhaPatrulhaVardann()