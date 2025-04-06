import os
import time

def fazendaConfronto():
    from resources.d20 import d20
    from player.inventario import inventory
    from player.status import Char
    from assets.itens import Itens
    from assets.data import itensPossuidos
    from areas.areas import areas
    from resources.duelo import duelo
    print("[1] - Conversar")
    print("[2] - Correr")
    print("[3] - Iniciar um duelo")
    option = input("Digite sua escolha: ")

    if not option.isdigit():
      os.system('cls')
      print("Opção inválida!")
      time.sleep(1)
      os.system('cls')
      return fazendaConfronto()
    else:
      option = int(option)
    
    if option == 1:
       os.system('cls')
       print("Aton conversou com o bandido e descobriu que ele também é de Eldoria.")
       time.sleep(2)
       print("Após minutos de conversa sobre o euller (ou adriano) nem chegarem a ler esse dialogo, o ladrão te recompensa com uma poção de ataque!")
       
       if itensPossuidos[0] == "":
        itensPossuidos[0] = Itens.venda[1]

       elif itensPossuidos[1] == "":
        itensPossuidos[1] = Itens.venda[1]

       elif itensPossuidos[2] == "":
        itensPossuidos[2] = Itens.venda[1]

       else:
         print("Você está com o inventário cheio e nao conseguiu carregar o item.")
       subOptions()
    elif option == 2:
       print("Para correr, é necessario tirar mais ou igual a 17 nos dados.")
       print("Rolando dados...")
       time.sleep(3)
       os.system('cls')
       resultadoDado = d20()
       print(f"Voce rolou: {resultadoDado}!")
       if resultadoDado >= 17:
          print("Aton consegue correr e sai ileso, voltando para o Centro da Cidade!")
          areas()
       else:
          print("Você não conseguiu correr, e um duelo foi iniciado!")
          duelo("Bandido", 60, 1.0)
          #continua se o jogador ficar vivo
          os.system('cls')
          print("Parabéns! você ganhou o duelo e 6 moedas foram adicionadas ao seu inventário!")
          print("Voltando ao Centro da Cidade...")
          Char.moedas += 6
          time.sleep(4)
          areas()
    elif option == 3:
       os.system('cls')
       print("Você decidiu duelar!")
       print("Preparando espadas...")
       time.sleep(2)
       os.system('cls')
       duelo("Bandido", 60, 1.0)
       os.system('cls')
       print("Parabéns! você ganhou o duelo e 6 moedas foram adicionadas ao seu inventário!")
       print("Voltando ao Centro da Cidade...")
       Char.moedas += 6
       time.sleep(4)
       areas()

def subOptions():
    from player.inventario import inventory
    from player.status import Char
    from assets.itens import Itens
    from assets.data import itensPossuidos
    from areas.areas import areas
    from resources.duelo import duelo
    print("\n[1] - Agradecer o bandido e ir embora.")
    print("[2] - Duelar contra o bandido em busca de ouro.")
    sub_option = input("Digite sua escolha: ")

    if not sub_option.isdigit():
        os.system('cls')
        print("Opção inválida!")
        time.sleep(1)
        return subOptions()

    sub_option = int(sub_option)
    
    if sub_option == 1:
        os.system('cls')
        print("Você agradece o bandido e segue seu caminho em paz.")
        time.sleep(2)
        areas()
    elif sub_option == 2:
        os.system('cls')
        print("Mesmo assim, você desafia o bandido para um duelo vida ou morte valendo ouro!")
        time.sleep(2)
        duelo("Bandido", 60, 1.1)
        #aqui só continua se o player ficar vivo
        os.system('cls')
        print("Parabéns! você ganhou o duelo e 6 moedas foram adicionadas ao seu inventário!")
        print("Voltando ao Centro da Cidade...")
        Char.moedas += 6
        time.sleep(4)
        areas()
    else:
        os.system('cls')
        print("Você selecionou uma opção inválida.")
        time.sleep(3)
        subOptions()
