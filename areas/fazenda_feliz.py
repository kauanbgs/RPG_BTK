import time
import os

def fazendaFeliz():
    from historia.fazendaConfronto import fazendaConfronto
    from player.status import Char
    from resources.menu import menu
    from areas.bosque_terrivel import bosqueTerrivel

    Char.veioFazenda = True
    print("Aton vê uma placa de sinalização, nela contém que a fazenda feliz está a 500 metros a direita. O guerreiro então, segue o caminho.")
    time.sleep(4)
    print("Após 3 minutos de caminhada, um arbusto emite um barulho estrondoso...")
    time.sleep(3)
    print("UM LADRÃO! o bandido sai do arbusto e te aborda! o que fazer?")
    fazendaConfronto()
