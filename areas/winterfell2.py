import time
import os

def winterfell2():
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

  os.system('cls')
  print("---Centro de Winterfell---")
  if Char.feito_mercador == True:
    print("[1] - Falar com o mercador mais próximo - FEITO")
  else:
    print("[1] - Falar com o mercador mais próximo")
  if Char.feito_castelo == True:
    print("[2] - Ir até o castelo falar com o lorde - FEITO")
  else:
    print("[2] - Ir até o castelo falar com o lorde")
  if Char.treinou_soldados == True:
    print("[3] - Treinar no campo com os soldados - FEITO")
  else:
    print("[3] - Treinar no campo com os soldados")
  if Char.conversou_moradores == True:
    print("[4] - Conversar com os moradores - FEITO")
  else:
    print("[4] - Conversar com os moradores")
  if Char.honra <= 1 or Char.conversou_moradores == False:
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