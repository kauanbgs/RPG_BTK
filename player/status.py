import time

class Char:
  charName = "Aton"
  vida = 100
  ataque = 1.3
  defesa = 1.0
  moedas = 1
  option = 0
  deadEnemy = False
  deadPlayer = False
  veioNoBosque = False
  where = "Eldoria"

def status():
    print(f"Nome: {Char.charName}")
    print(f"Vida: {Char.vida}")
    print(f"Ataque: {Char.ataque}")
    print(f"Defesa: {Char.defesa}")
    print(f"Moedas: {Char.moedas}")
    time.sleep(2)