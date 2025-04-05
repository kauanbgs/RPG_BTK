import time
import os

from player.status import Char
from resources.d20 import d20

def apostaDados():
  print("Insira [0] para voltar!")
  print("Você irá jogar uma rodada de aposta de dados!\nAs regras são as seguintes: Voce irá rolar um dado de 20 lados, se cair mais ou igual a 10 suas moedas se multiplicam em 1.5, se cair menos você perde todas as moedas apostadas.")
  aposta = int(input("Quanto quer apostar: "))
  if aposta == 0:
    from areas.bosque_terrivel import bosqueTerrivel
    bosqueTerrivel()
  elif aposta > Char.moedas:
    print("Você não tem moedas suficientes para apostar isso!")
    time.sleep(2)
    os.system('cls')
    apostaDados()
  else:
    resultadoDado = d20()
    if resultadoDado >= 10:
      Char.moedas = Char.moedas * 1.5
      print(f"O dado rolou: {resultadoDado}")
      print(f"Você ganhou! Você agora tem {Char.moedas} moedas!")
      time.sleep(4)
      os.system('cls')
      apostaDados()
    else:
      Char.moedas -= aposta
      print(f"O dado rolou: {resultadoDado}")
      print(f"Você perdeu! Você agora tem {Char.moedas} moedas!")
      time.sleep(4)
      os.system('cls')
      apostaDados()
