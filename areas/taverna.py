from assets.itens import Itens
from player.status import Char

def taverna():
  from player.inventario import inventory
  from assets.data import itensPossuidos
  from resources.menu import menu

  print("Você entrou na taverna!")
  print(f"Você tem {Char.moedas} moedas!")
  print("[0] - Voltar")
  print(f"[1] - {Itens.venda[0]} - 5 moedas")
  print(f"[2] - {Itens.venda[1]} - 3 moedas")
  print(f"[3] - {Itens.venda[2]} - 3 moedas")
  option = int(input("Escolha uma opção: "))

  if option == 0:
    menu()
  elif option == 1:
    if itensPossuidos[0] == "":
      if Char.moedas >= 5:
        itensPossuidos[0] = Itens.venda[0]
        print(f"Você comprou {Itens.venda[0]}!")
        Char.moedas -= 5
      else:
        print("Você não tem moedas suficientes!")
        taverna()
    elif itensPossuidos[1] == "":
      if Char.moedas >= 5:
        itensPossuidos[1] = Itens.venda[0]
        print(f"Você comprou {Itens.venda[0]}!")
        Char.moedas -= 5
      else:
        print("Você não tem moedas suficientes!")
        taverna()
    elif itensPossuidos[2] == "":
      if Char.moedas >= 5:
        itensPossuidos[2] = Itens.venda[0]
        print(f"Você comprou {Itens.venda[0]}!")
        Char.moedas -= 5
      else:
        print("Você não tem moedas suficientes!")
        taverna()
  elif option == 2:
    if itensPossuidos[0] == "":
      if Char.moedas >= 3:
        itensPossuidos[0] = Itens.venda[1]
        print(f"Você comprou {Itens.venda[1]}!")
        Char.moedas -= 3
      else:
        print("Você não tem moedas suficientes!")
        taverna()
    elif itensPossuidos[1] == "":
      if Char.moedas >= 3:
        itensPossuidos[1] = Itens.venda[1]
        print(f"Você comprou {Itens.venda[1]}!")
        Char.moedas -= 3
      else:
        print("Você não tem moedas suficientes!")
        taverna()
    elif itensPossuidos[2] == "":
      if Char.moedas >= 3:
        itensPossuidos[2] = Itens.venda[1]
        print(f"Você comprou {Itens.venda[1]}!")
        Char.moedas -= 3
      else:
        print("Você não tem moedas suficientes!")
        taverna()
  elif option == 3:
    if itensPossuidos[0] == "":
      if Char.moedas >= 3:
        itensPossuidos[0] = Itens.venda[2]
        print(f"Você comprou {Itens.venda[2]}!")
        Char.moedas -= 3
      else:
        print("Você não tem moedas suficientes!")
        taverna()
    elif itensPossuidos[1] == "":
      if Char.moedas >= 3:
        itensPossuidos[1] = Itens.venda[2]
        print(f"Você comprou {Itens.venda[2]}!")
        Char.moedas -= 3
      else:
        print("Você não tem moedas suficientes!")
        taverna()
    elif itensPossuidos[2] == "":
      if Char.moedas >= 3:
        itensPossuidos[2] = Itens.venda[2]
        print(f"Você comprou {Itens.venda[2]}!")
        Char.moedas -= 3
      else:
        print("Você não tem moedas suficientes!")
        taverna()
  else:
    print("Opção inválida!")
    taverna()
