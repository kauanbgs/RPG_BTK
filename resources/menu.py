while True:
  print("------------------Menu-----------------")
  print("[1] - Inventário")
  print("[2] - Status")
  print("[3] - Taverna")
  print("[4] - Explorar")
  option = int(input("Escolha uma opção: "))
  if option not in [1, 2, 3, 4]:
    print("Opção inválida!")
    break
  elif option == 1:
    inventory()
  elif option == 2:
    status()
  elif option == 3:
    taverna()
  elif option == 4:
    explorar()