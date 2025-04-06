from player.status import Char
import os
import time

def areas():
  from areas.bosque_terrivel import bosqueTerrivel
  from areas.bosque_terrivel2 import bosqueTerrivel2
  from areas.fazenda_feliz import fazendaFeliz
  from resources.menu import menu
  Char.where = "Centro da Cidade"
  print(f"Você está atualmente no: {Char.where}")
  print("Você pode ir para:")
  print("[0] - Voltar ao menu")
  print("[1] - Bosque Terrível")
  print("[2] - Fazenda Feliz")
  opcao = int(input("Escolha uma opção: "))
  if opcao == 0:
    os.system('cls')
    print("Voltando ao centro da cidade...")
    time.sleep(1)
    menu()
  elif opcao == 1:
    if Char.veioNoBosque == True:
      Char.where = "Bosque Terrível"
      os.system('cls')
      bosqueTerrivel2()
    else:
      Char.where = "Bosque Terrível"
      os.system('cls')
      bosqueTerrivel()
  elif opcao == 2:
    Char.where = "Fazenda Feliz"
    os.system('cls')
    fazendaFeliz()