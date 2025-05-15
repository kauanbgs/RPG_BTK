from player.status import Char
import os
import time
from assets.data import limpar_tela


def areas():
  from areas.bosque_terrivel import bosqueTerrivel
  from areas.bosque_terrivel2 import bosqueTerrivel2
  from areas.fazenda_feliz import fazendaFeliz
  from areas.winterfell import winterfell
  from areas.postoVardann import postoVardann
  from areas.postoVardann import postoVardannIntro
  from resources.menu import menu
  limpar_tela()
  Char.where = "Centro da Cidade"
  print(f"Você está atualmente no: {Char.where}\n")
  print("Você pode ir para: \n")
  print("[0] - Voltar ao menu")
  print("[1] - Bosque Terrível")
  if Char.veioFazenda == True:
    print("[2] - Fazenda Feliz - FEITO")
  else:
    print("[2] - Fazenda Feliz")
  if Char.veioFazenda == True and Char.veioWinterfell == False:
    print("[3] - Vila Winterfell - DESBLOQUEADO")
  elif Char.veioWinterfell == True:
    print("[3] - Vila Winterfell - FEITO")
  if Char.veioWinterfell == True and Char.veioVardann == False:
    print("[4] - Posto de Vardann - DESBLOQUEADO")
  elif Char.veioVardann == True:
    print("[4] - Posto de Vardann - FEITO")
  

  
    
  option = input("Escolha uma opção: ")

  if not option.isdigit():
    limpar_tela()
    print("Opção inválida!")
    time.sleep(1)
    areas()
  else:
    option = int(option)

  if option == 0:
    limpar_tela()
    print("Voltando ao centro da cidade...")
    time.sleep(1)
    menu()
  elif option == 1:
    if Char.veioNoBosque == True:
      Char.where = "Bosque Terrível"
      limpar_tela()
      bosqueTerrivel2()
    else:
      Char.where = "Bosque Terrível"
      limpar_tela()
      bosqueTerrivel()
  elif option == 2:
    if Char.veioFazenda == True:
      print("Você já fez essa side quest!")
      time.sleep(2)
      limpar_tela()
      areas()
    else:
      Char.where = "Fazenda Feliz"
      limpar_tela()
      fazendaFeliz()
  elif option == 3:
    if Char.veioFazenda == False:
      limpar_tela()
      print("Você não desbloqueou essa ilha!")
      time.sleep(1)
      areas()
    if Char.veioWinterfell == True:
      limpar_tela
      print("Você já fez essa quest!")
      time.sleep(1)
      areas()
    else:
      Char.where = "Winterfell"
      limpar_tela
      winterfell()
  elif option == 4:
    if Char.veioVardann == False:
      Char.where = "Vardann"
      postoVardannIntro()
      postoVardann()
    else:
      print("Você já fez essa quest!")
      time.sleep(1)
      areas()

  else:
    limpar_tela()
    print("Opção não existente.")
    time.sleep(1)
    areas()