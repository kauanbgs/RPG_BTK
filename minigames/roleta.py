from resources.d20 import d20
from player.status import Char

import time
import os

def roleta():
  from random import randint
  os.system('cls')
  print("Você chegou na roleta! as regras são as seguintes:")
  print("Você irá jogar uma rodada de roleta, se você acertar uma tripla você ganha 5 moedas, se acertar um par você ganha 3 moedas, se não acertar nada você perde 2 moedas.")
  print("Insira [0] para voltar!")
  print("Insira [1] para jogar!")
  option = int(input("Escolha uma opção: "))
  if option == 0:
    from areas.bosque_terrivel2 import bosqueTerrivel2
    bosqueTerrivel2()
  elif option == 1:

    if Char.moedas <= 2:
      print("Você não tem moedas suficientes para jogar.")
      time.sleep(2)
      os.system('cls')
      roleta()
    print("Girando a roleta...")
    time.sleep(2)
    os.system('cls')


    resultadoDado = d20()

    numeros = [randint(1, 9), randint(1, 9), randint(1, 9)]

    if numeros[0] == numeros[1] and numeros[1] == numeros[2]:
      print(f"{numeros[0]} - {numeros[1]} - {numeros[2]}")
      print("Você acertou uma tripla! foram adicionadas 5 moedas ao seu inventário.")
      Char.moedas += 5
      print(f"Você agora tem {Char.moedas} de ouro.")
      time.sleep(5)
      roleta()
    elif numeros[0] == numeros[1] or numeros[1] == numeros[2] or numeros[0] == numeros[2]:
      print(f"{numeros[0]} - {numeros[1]} - {numeros[2]}")
      print("Você acertou um par! foram adicionadas 3 moedas ao seu inventário.")
      Char.moedas += 3
      print(f"Você agora tem {Char.moedas} de ouro.")
      time.sleep(5)
      roleta()
    else:
      print(f"{numeros[0]} - {numeros[1]} - {numeros[2]}")
      print("Você não acertou nada! 2 moedas foram retiradas do seu inventário.")
      Char.moedas -= 2
      if Char.moedas < 0:
        Char.moedas = 0
      print(f"Você agora tem {Char.moedas} de ouro.")
      time.sleep(5)
      roleta()


