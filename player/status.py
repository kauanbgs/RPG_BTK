import time

class Char:
  charName = "Aton"
  vida = 100
  ataque = 1.3
  arma = ""
  defesa = 1.0
  moedas = 50
  option = 0
  deadEnemy = False
  deadPlayer = False
  veioNoBosque = False
  veioFazenda = False
  where = "Eldoria"

  def atualizar_ataque():
    base = 1.3
    if Char.arma == "Espada de Madeira":
      Char.ataque = base + 0.5
    elif Char.arma == "Espada de Prata":
      Char.ataque = base + 1.0
    elif Char.arma == "Espada de Ouro":
      Char.ataque = base + 1.5
    else:
      Char.ataque = base

def status():
    print(f"Nome: {Char.charName}")
    print(f"Vida: {Char.vida}")
    if Char.arma == "":
       print("Arma: Mãos")
    else:
      print(f"Arma: {Char.arma}")
    print(f"Ataque: {Char.ataque}")
    print(f"Defesa: {Char.defesa}")
    print(f"Moedas: {Char.moedas}")
    time.sleep(5)