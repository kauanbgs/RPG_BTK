import os
import time
from resources.d20 import d20
from resources.duelo import duelo
from areas.taverna import taverna
from player.status import Char
from player.inventario import inventory
from resources.menu import menu
from historia.inicio import paginaInicial
from minigames.adivinhacao import jogo_adivinhacao
from minigames.aposta_dados import apostaDados
from minigames.roleta import roleta
from minigames.anagrama import anagrama
from minigames.reflexo import jogoReflexo
from areas.ferreiro import ferreiro
from areas.areas import areas
from areas.winterfell import winterfell
from historia.histWinterfell import tribunal

def main():
  paginaInicial()

main()