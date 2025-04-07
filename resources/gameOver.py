def gameOver():
    from assets import game_state
    from player.status import Char
    import os
    import time

    os.system('cls')
    print("======== GAME OVER ========")

    tempoTotal = time.time() - game_state.tempoComeco
    minutos = int(tempoTotal // 60)
    segundos = int(tempoTotal % 60)

    print(f" Tempo de jogo: {minutos:.2f} minuto(s) e {segundos} segundo(s)")
    print(f"Personagem: {Char.charName}")
    print(f"Ataque Final: {Char.ataque:.2f}")
    print(f"Defesa Final: {Char.defesa:.2f}")
    print(f"Ouro Acumulado: {Char.moedas}")

    print("\nObrigado por jogar!")
    print("Sua jornada pode ter acabado... mas as lendas permanecem.")
    time.sleep(6)
    exit()