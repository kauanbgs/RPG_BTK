from player.status import Char

import os
import time

def venderArma():
  from areas.ferreiro import ferreiro
  from areas.areas import areas

  os.system('cls')
  print("Vender itens devolve o dinheiro pela metade!(Arredondado pra cima)")
  time.sleep(1)
  option = input(f"Você atualmente tem uma {Char.arma}, deseja realmente vender? [s/n]: ")
  if option == "s":
    if Char.arma == "Espada de Madeira":
      Char.arma = ""
      Char.moedas += 3
      os.system('cls')
      print("Foram adicionadas 3 Moedas ao seu inventário!")
      time.sleep(2)
      os.system('cls')
      ferreiro()

    elif Char.arma == "Espada de Prata":
      Char.arma = ""
      Char.moedas += 5
      os.system('cls')
      print("Foram adicionadas 5 Moedas ao seu inventário!")
      time.sleep(2)
      os.system('cls')
      ferreiro()
    elif Char.arma == "Espada de Ouro":
      Char.arma = ""
      Char.moedas += 10
      os.system('cls')
      print("Foram adicionadas 10 Moedas ao seu inventário!")
      time.sleep(2)
      os.system('cls')
      ferreiro()
  elif option == "n":
    os.system('cls')
    print("Voltando ao Centro da Cidade...")
    os.system('cls')
    areas()
  else:
    os.system('cls')
    print("Opção invalida!")
    time.sleep(1)
    os.system('cls')
    venderArma()


  
  