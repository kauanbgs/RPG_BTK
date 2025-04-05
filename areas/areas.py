from player.status import Char



def areas():
  from areas.bosque_terrivel import bosqueTerrivel
  from resources.menu import menu
  print(f"Você está atualmente em:{Char.where}")
  print("Você pode ir para:")
  print("[0] - Voltar")
  print("[1] - Bosque Terrível")
  print("[2] - Fazenda Feliz")
  opcao = int(input("Escolha uma opção: "))
  if opcao == 0:
    menu()
  elif opcao == 1:
    Char.where = "Bosque Terrível"
    bosqueTerrivel()