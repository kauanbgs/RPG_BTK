from player.status import Char
import os
import time

def areas():
  from areas.bosque_terrivel import bosqueTerrivel
  from areas.bosque_terrivel2 import bosqueTerrivel2
  from areas.fazenda_feliz import fazendaFeliz
  from areas.winterfell import winterfell
  from resources.menu import menu
  os.system('cls')
  Char.where = "Centro da Cidade"
  print(f"Você está atualmente no: {Char.where}")
  print("Você pode ir para:")
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

  
    
  option = input("Escolha uma opção: ")

  if not option.isdigit():
    os.system('cls')
    print("Opção inválida!")
    time.sleep(1)
    areas()
  else:
    option = int(option)

  if option == 0:
    os.system('cls')
    print("Voltando ao centro da cidade...")
    time.sleep(1)
    menu()
  elif option == 1:
    if Char.veioNoBosque == True:
      Char.where = "Bosque Terrível"
      os.system('cls')
      bosqueTerrivel2()
    else:
      Char.where = "Bosque Terrível"
      os.system('cls')
      bosqueTerrivel()
  elif option == 2:
    if Char.veioFazenda == True:
      print("Você já fez essa side quest!")
      time.sleep(2)
      os.system('cls')
      return areas()
    else:
      Char.where = "Fazenda Feliz"
      os.system('cls')
      fazendaFeliz()
  elif option == 3:
    if Char.veioWinterfell == True:
      print("Você já fez essa quest!")
      areas()
    else:
      Char.where = "Winterfell"
      os.system('cls')
      winterfell()