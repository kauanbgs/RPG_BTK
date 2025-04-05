from player.inventario import inventory
from player.status import Char
from player.status import status
from assets.itens import Itens
from areas.taverna import taverna
from areas.areas import areas


def menu():
  while True:
    print("------------------Menu-----------------")
    print("[1] - Inventário")
    print("[2] - Status")
    print("[3] - Taverna")
    print("[4] - Explorar")
    option = int(input("Escolha uma opção: "))
    if option not in [1, 2, 3, 4]:
      print("Opção inválida!")
      continue
    elif option == 1:
      inventory()
    elif option == 2:
      status()
    elif option == 3:
      taverna()
    elif option == 4:
      areas()