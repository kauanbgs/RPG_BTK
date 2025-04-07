import time
import os



def winterfell():
  from areas.winterfell2 import winterfell2
  from areas.areas import areas
  from player.status import Char
  from resources.menu import menu
  from historia.histWinterfell import investigar_mercador
  from historia.histWinterfell import investigar_castelo
  from historia.histWinterfell import treinar_com_soldados
  from historia.histWinterfell import conversar_com_moradores
  from historia.histWinterfell import tribunal
  Char.veioWinterfell = True
  print("Depois de dias de viagem e noites frias, Aton finalmente avista os portões de Winterfell ao longe.")
  time.sleep(5)
  print("Uma névoa espessa cobre as muralhas de pedra, e corvos sobrevoam o céu cinzento.")
  time.sleep(5)
  print("Ao se aproximar, dois soldados o barram. 'Identifique-se!', diz um deles, com a mão na empunhadura da espada.")
  time.sleep(5)
  print("Aton se apresenta com firmeza. Os soldados se entreolham e liberam a passagem.")
  time.sleep(5)
  print("Assim que atravessa os portões, Aton sente o clima pesado. Olhares desconfiados, sussurros em cada canto.")
  time.sleep(5)
  print("Algo está errado em Winterfell...")
  time.sleep(5)
  os.system('cls')
  print("---Centro de Winterfell---")
  print("[1] - Falar com o mercador mais próximo")
  print("[2] - Ir até o castelo falar com o lorde")
  print("[3] - Treinar no campo com os soldados")
  print("[4] - Conversar com os moradores")
  if Char.honra <= 2 or Char.conversou_moradores == False:
    print("[5] - Tribunal (NAO RECOMENDADO)")
  else:
    print("[5] - Tribunal")
  
  escolha = input("Escolha uma opção: ")
  
  if escolha == "1":
    investigar_mercador()
  elif escolha == "2":
    investigar_castelo()
  elif escolha == "3":
    treinar_com_soldados()
  elif escolha == "4":
    conversar_com_moradores()
  elif escolha == "5":
    tribunal()
  else:
      print("\nOpção inválida. Tente novamente.\n")
      time.sleep(2)
      winterfell2()