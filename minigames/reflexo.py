import random
import time
import os
from areas.bosque_terrivel2 import bosqueTerrivel2
from player.status import Char

def jogoReflexo():
    print("Bem-vindo ao jogo do reflexo! para ganhar, você terá que apertar o botão [ENTER] o mais rápido possível!")
    print(f"Você tem {Char.moedas} moedas.")
    print("Quer jogar? s/n")
    option = input("Escolha uma opção: ").lower()
    if option == "s":
      if Char.moedas > 3:
          print("Se prepare!")
          time.sleep(random.randint(2, 7))
          os.system('cls')
          print("JÁ!!!!!!!!!!!!")
          start_time = time.time()
          input("")
          end_time = time.time()
          reaction_time = end_time - start_time
          print(f"Seu tempo de reação foi de {reaction_time:.2f} segundos.")
          if reaction_time < 0.20:
              print("Você é muito rápido! ganhou 4 moedas!")
              Char.moedas += 4
              time.sleep(2)
              os.system('cls')
              jogoReflexo()
          elif reaction_time < 0.23:
              print("Você é rápido! ganhou 3 moedas!")
              Char.moedas += 3
              time.sleep(2)
              os.system('cls')
              jogoReflexo()
          elif reaction_time < 0.26:
              print("Parabéns! ganhou 2 moedas!")
              Char.moedas += 2
              time.sleep(2)
              os.system('cls')
              jogoReflexo()
          elif reaction_time < 0.29:
              print("Você é lento! ganhou 1 moeda!")
              Char.moedas += 1
              time.sleep(2)
              os.system('cls')
              jogoReflexo()
          elif reaction_time < 0.33:
              print("Você é muito lento! perdeu 3 moedas!")
              Char.moedas -= 3
              if Char.moedas < 0:
                  Char.moedas = 0
              time.sleep(2)
              os.system('cls')
              jogoReflexo()
          elif reaction_time <= 0.37:
              print("Você é muito lento! perdeu 5 moedas!")
              Char.moedas -= 5
              if Char.moedas < 0:
                  Char.moedas = 0
              time.sleep(2)
              os.system('cls')
              jogoReflexo()
          elif reaction_time > 0.41:
              print("Você é MUITO lento! perdeu 6 moedas!")
              Char.moedas -= 6
              if Char.moedas < 0:
                  Char.moedas = 0
              time.sleep(2)
              os.system('cls')
              jogoReflexo()
      else:
          print("Você não tem moedas suficientes para jogar.")
          time.sleep(2)
          os.system('cls')
          jogoReflexo()
    elif option == "n":
      print("Ok, obrigado por jogar!")
      time.sleep(2)
      os.system('cls')
      bosqueTerrivel2()
    else:
      print("Opção inválida! Tente novamente.")
      time.sleep(1)
      os.system('cls')
      jogoReflexo()
         