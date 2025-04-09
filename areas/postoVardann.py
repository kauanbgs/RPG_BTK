import time
import os
from areas.areas import areas
from player.status import Char
from resources.menu import menu

def postoVardannIntro():
  Char.veioVardann = True
  os.system('cls')
  print("Após ter se destacado em Winterfell, Aton é convidado para escoltar uma caravana de suprimentos até o posto avançado de Vardann.")
  time.sleep(4)
  print("Vardann é uma ilha montanhosa, isolada e estratégica, porém constantemente ameaçada por bandidos e mercenários...")
  time.sleep(4)
  