from player.status import Char

def jogo_adivinhacao():
    import random
    counter = 0
    words = ["python", "programacao", "computador", "jogo", "adivinhacao", "kauan", "gamer", 
    "desenvolvedor", "programador", "tecnologia", "software", "hardware", "internet", 
    "rede", "dados", "algoritmo", "sistema", "aplicativo", "mobile", "web", "front-end", 
    "back-end", "euller", "matematica", "fisica", "quimica", "biologia", "geografia", 
    "historia", "portugues", "ingles", "espanhol", "frances", "italiano", "alemao", 
    "russo", "japones", "chines", "coreano", "arabe", "hebraico",
    "logica", "codigo", "terminal", "framework", "linguagem", "interface", "usuario", 
    "banco", "servidor", "nuvem", "compilador", "debug", "teste", "inteligencia", 
    "artificial", "robotica", "analise", "dados", "estatistica", "criptografia", 
    "seguranca", "informacao", "bit", "byte", "memoria", "processador", "placa", 
    "fonte", "monitor", "teclado", "mouse", "arduino", "raspberry", "iot", "rede", 
    "local", "internet", "wifi", "ethernet", "navegador", "chrome", "firefox", 
    "explorer", "edge", "opera", "safari", "linux", "windows", "ubuntu", "android", 
    "ios", "google", "apple", "microsoft", "openai", "chatgpt", "modelo", "neural", 
    "treinamento", "dataset", "token", "loop", "condicional", "variavel", "constante", 
    "funcao", "classe", "objeto", "metodo", "modulo", "pacote", "biblioteca", 
    "git", "github", "commit", "push", "pull", "merge", "branch", "clone", 
    "pip", "venv", "virtualenv", "notebook", "colab", "visualstudio", "pycharm", 
    "sublime", "vscode", "terminal", "linha", "comando", "deploy", "api", "json", 
    "xml", "html", "css", "javascript", "typescript", "node", "react", "angular", 
    "vue", "bootstrap", "jquery", "php", "sql", "postgres", "mysql", "sqlite", 
    "mongodb", "firebase", "backlog", "scrum", "kanban", "sprint", "trello", 
    "jira", "figma", "prototipo", "ux", "ui", "layout", "wireframe", "responsivo"]
    print("-------------------------------------------------")
    print("Bem-vindo ao jogo de adivinhação! Você terá 5 tentativas para adivinhar a palavra secreta, e pode perder moedas!")
    print("Quer jogar? s/n")
    option = input("Escolha uma opção: ").lower()
    if option == "s":
      if Char.moedas > 5:
        choice = random.choice(words)
        print(f'Dica inicial: a palavra tem {len(choice)} letras.')
        escolha = input("Chute: ").lower()
        if escolha == choice:
            print(f"VOCE ACERTOU DE PRIMEIRA!, e ganhou 30 moedas!")
            Char.moedas += 30
            words.remove(choice)
            jogo_adivinhacao()
        else:
            print(f"Você errou, e perdeu 1 moeda! Proxima dica: a primeira letra da palavra é: {choice[0]}")
            counter += 1
            Char.moedas -= 1
            escolha = input("Chute: ").lower()
            if escolha == choice:
              print(f"Você acertou, e ganhou 10 moedas!")
              Char.moedas += 10
              words.remove(choice)
              jogo_adivinhacao
            else:
              print(f"Você errou, e perdeu 1 moeda! Proxima dica: a ultima letra da palavra é: {choice[-1]}")
              counter += 1
              Char.moedas -= 1
              escolha = input("Chute: ").lower()
              if escolha == choice:
                print(f"Você acertou, e ganhou 7 moedas!")
                Char.moedas += 7
                words.remove(choice)
                jogo_adivinhacao()
              else:
                print(f"Voce errou, e perdeu 1 moeda! Proxima dica: a palavra tem {choice.count('a')} letras 'a'")
                counter += 1
                Char.moedas -= 1
                escolha = input("Chute: ").lower()
                if escolha == choice:
                  print(f"Você acertou, e ganhou 5 moedas!")
                  Char.moedas += 5
                  words.remove(choice)
                  jogo_adivinhacao()
                else:
                  print(f"Você errou, e perdeu 1 moeda! Proxima dica: a segunda letra da palavra é: {choice[1]}")
                  counter += 1
                  Char.moedas -= 1
                  escolha = input("Chute: ").lower()
                  if escolha == choice:
                    print(f"Você acertou, e ganhou 3 moedas!")
                    Char.moedas += 3
                    words.remove(choice)
                    jogo_adivinhacao()
                  else:
                    print(f"Você perdeu, e perdeu 2 moedas! a palavra era: {choice}")
                    Char.moedas -= 1
                    words.remove(choice)
                    if Char.moedas < 0:
                      Char.moedas = 0
                    jogo_adivinhacao()
      else:
        print("Você não tem moedas suficientes para jogar.")
        return
    elif option == "n":
      print("Você decidiu não jogar.")
      from areas.bosque_terrivel2 import bosqueTerrivel2
      bosqueTerrivel2()


      