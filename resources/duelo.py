from resources.d20 import d20
from player.status import Char
from resources.gameOver import gameOver
import time
import os

def duelo(nomeInimigo, vidainimigo, ataqueInimigo):

  while (Char.vida > 0 and vidainimigo > 0):
    os.system('cls')  # limpa a tela no início de cada rodada

    print(f"---DUELO CONTRA: {nomeInimigo}---")
    print(f"{nomeInimigo}---{vidainimigo:.2f}HP---{ataqueInimigo}ATK")
    print(f"{Char.charName}---{Char.vida:.2f}HP---{Char.ataque}ATK")
    print("------------------Vez do jogador------------------")
    print("[1] - Atacar")
    print("[2] - Defender")
    print("[3] - Correr")
    option = input("Escolha uma opção: ")

    if not option.isdigit():
      os.system('cls')
      print("Opção inválida!")
      time.sleep(1)
      continue

    option = int(option)

    if option not in [1, 2, 3]:
      os.system('cls')
      print("Opção inválida! Escolha entre 1, 2 ou 3.")
      time.sleep(1)
      continue

    if option == 1:
      resultadoDado = d20()
      print("Você decidiu atacar!")
      print(f"O dado rolou: {resultadoDado}, seu ataque foi multiplicado por: {Char.ataque}")
      dano = Char.ataque * resultadoDado
      vidainimigo -= dano
      print(f"Dano causado: {dano:.2f}!")
      time.sleep(3)

      if vidainimigo <= 0:
        print(f"{nomeInimigo} foi derrotado!")
        time.sleep(4)
        break

    elif option == 2:
      resultadoDado = d20()
      print("Voce decidiu defender, e ganhou um buff temporario de defesa!")
      Char.defesa += 0.3
      print(f"O dado rolou: {resultadoDado} para o inimigo, sua defesa foi multiplicada por: {Char.defesa}")
      dano = ataqueInimigo * resultadoDado / Char.defesa
      Char.defesa -= 0.3
      print(f"Dano sofrido: {dano}!")
      Char.vida -= dano
      time.sleep(2)
      if Char.vida <= 0:
        print(f"{Char.charName} foi derrotado!, e o jogo acabou")
        time.sleep(4)
        gameOver()

    elif option == 3:
      print("Você decidiu correr!")
      resultadoDado = d20()
      if resultadoDado >= 19:
        print("Você conseguiu fugir!")
        break
      else:
        print("Você não conseguiu fugir!")
        resultadoDado = d20()
        print(f"O dado rolou: {resultadoDado} para o inimigo, sua defesa foi multiplicada por: {Char.defesa}")
        dano = ataqueInimigo * resultadoDado / Char.defesa
        Char.vida -= dano
        time.sleep(4)
        if Char.vida <= 0:
          print(f"{Char.charName} foi derrotado!, e o jogo acabou!")
          time.sleep(4)
          gameOver()

    if vidainimigo > 0:
      print("------------------Vez do inimigo-----------------")
      print("Agora é a vez do inimigo!")
      resultadoDado = d20()
      print(f"O dado rolou: {resultadoDado} para o inimigo, seu ataque foi multiplicado por: {ataqueInimigo}")
      dano = ataqueInimigo * resultadoDado
      Char.vida -= dano
      print(f"Dano sofrido: {dano}!")
      time.sleep(4)
      if Char.vida <= 0:
        print(f"{Char.charName} foi derrotado!, e o jogo acabou!")
        time.sleep(4)
        gameOver()
