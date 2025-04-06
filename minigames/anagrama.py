import random
import time
import os
from areas.bosque_terrivel2 import bosqueTerrivel2
from player.status import Char

def embaralhar_palavra(palavra):
    letras = list(palavra)
    embaralhada = palavra
    while embaralhada == palavra:
        random.shuffle(letras)
        embaralhada = ''.join(letras)
    return embaralhada

def anagrama():
    palavras = ["python", "programacao", "computador", "jogo", "adivinhacao", "kauan", "gamer",
        "desenvolvedor", "programador", "tecnologia", "software", "hardware", "internet",
        "rede", "dados", "algoritmo", "sistema", "aplicativo", "mobile", "web", "front-end",
        "back-end", "euller", "matematica", "fisica", "quimica", "biologia", "geografia",
        "historia", "portugues", "ingles", "espanhol", "frances", "italiano", "alemao",
        "russo", "japones", "chines", "coreano", "arabe", "hebraico", "logica", "codigo",
        "terminal", "framework", "linguagem", "interface", "usuario", "banco", "servidor",
        "nuvem", "compilador", "debug", "teste", "inteligencia", "artificial", "robotica",
        "analise", "estatistica", "criptografia", "seguranca", "informacao", "bit", "byte",
        "memoria", "processador", "placa", "fonte", "monitor", "teclado", "mouse", "arduino",
        "raspberry", "iot", "local", "wifi", "ethernet", "navegador", "chrome", "firefox",
        "explorer", "edge", "opera", "safari", "linux", "windows", "ubuntu", "android",
        "ios", "google", "apple", "microsoft", "openai", "chatgpt", "modelo", "neural",
        "treinamento", "dataset", "token", "loop", "condicional", "variavel", "constante",
        "funcao", "classe", "objeto", "metodo", "modulo", "pacote", "biblioteca", "git",
        "github", "commit", "push", "pull", "merge", "branch", "clone", "pip", "venv",
        "virtualenv", "notebook", "colab", "visualstudio", "pycharm", "sublime", "vscode",
        "linha", "comando", "deploy", "api", "json", "xml", "html", "css", "javascript",
        "typescript", "node", "react", "angular", "vue", "bootstrap", "jquery", "php", "sql",
        "postgres", "mysql", "sqlite", "mongodb", "firebase", "backlog", "scrum", "kanban",
        "sprint", "trello", "jira", "figma", "prototipo", "ux", "ui", "layout", "wireframe",
        "responsivo"
    ]

    while True:
        os.system('cls')
        print("===== MINIGAME: ANAGRAMA =====")
        print("Insira [0] para voltar")
        print("Quer jogar anagramas? (s/n)")
        option = input("Escolha uma opção: ").lower()

        if option == "0":
            print("Voltando...")
            time.sleep(2)
            os.system('cls')
            bosqueTerrivel2()
            return

        elif option == "n":
            os.system('cls')
            print("Ok, obrigado por jogar!.")
            time.sleep(2)
            bosqueTerrivel2()
            return

        elif option == "s":
            if Char.moedas < 2:
                print("Você não tem moedas suficientes para jogar.")
                time.sleep(2)
                continue  # volta pro menu do jogo

            palavra_escolhida = random.choice(palavras)
            palavra_embaralhada = embaralhar_palavra(palavra_escolhida)

            print(f"\nA palavra embaralhada é: {palavra_embaralhada}")
            chute = input("Adivinhe a palavra: ").lower()

            if chute == palavra_escolhida:
                print(f"Você acertou! A palavra era '{palavra_escolhida}' e você ganhou 2 moedas.")
                Char.moedas += 2
            else:
                print(f"Você errou! A palavra era '{palavra_escolhida}' e você perdeu 4 moedas.")
                Char.moedas -= 4
                if Char.moedas < 0:
                    Char.moedas = 0

            time.sleep(3)
        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(2)
