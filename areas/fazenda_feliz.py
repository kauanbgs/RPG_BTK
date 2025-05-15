import time
import os

from assets.data import printDigitado
from assets.config import config

def fazendaFeliz():
    from historia.fazendaConfronto import fazendaConfronto
    from player.status import Char
    from resources.menu import menu
    from areas.bosque_terrivel import bosqueTerrivel

    Char.veioFazenda = True
    printDigitado("Aton vê uma placa de sinalização, nela contém que a fazenda feliz está a 500 metros a direita. O guerreiro então, segue o caminho.\n", config.tempo)
    time.sleep(4)
    printDigitado("Após 3 minutos de caminhada, um arbusto emite um barulho estrondoso...\n", config.tempo)
    time.sleep(3)
    printDigitado("UM LADRÃO! o bandido sai do arbusto e te aborda! o que fazer?\n", config.tempo)
    fazendaConfronto()
