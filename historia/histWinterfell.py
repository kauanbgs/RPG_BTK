import time
from player.status import Char
from resources.d20 import d20
from areas.areas import areas
from areas.winterfell import winterfell
from areas.winterfell2 import winterfell2

def investigar_mercador():
    if Char.feito_mercador == True:
        print("Você já conversou com o mercador. Ele apenas balança a cabeça, ocupado com seus negócios.")
        time.sleep(2)
        winterfell2()

    print("Você se aproxima do mercador, que organiza suas mercadorias com mãos tremulas.")
    time.sleep(3)
    print("Ele ergue os olhos e reconhece Aton pela armadura. 'Você... é de Skalice, não é?'")
    time.sleep(4)
    print("Após uma breve conversa, o mercador confessa ter ouvido um som estranho vindo dos fundos da muralha durante a noite do crime.")
    time.sleep(4)
    print("'Não vi ninguém... Mas ouvi passos. Apressados. E depois, silêncio.'")
    time.sleep(3)
    print("Essa informação pode ser útil no tribunal.")
    time.sleep(6)

    Char.pistas.append("Som estranho vindo dos fundos da muralha")
    Char.feito_mercador = True
    winterfell2()


def investigar_castelo():
    if Char.feito_castelo == True:
        print("Você já esteve no castelo hoje. O Lorde está ocupado com os preparativos do julgamento.")
        time.sleep(2)
        winterfell2()

    print("Você caminha até o castelo de Winterfell, imponente mesmo sob a névoa.")
    time.sleep(3)
    print("Guardas abrem os portões lentamente. Aton é levado até o salão principal.")
    time.sleep(3)
    print("O Lorde da cidade o encara por longos segundos antes de falar.")
    time.sleep(3)
    print("'Aton de Skalice... Já ouvi falar de você. Preciso de olhos confiáveis esta noite.'")
    time.sleep(4)
    print("'Vigie os corredores durante a madrugada. Quero saber se algum de meus próprios homens está envolvido no crime.'")
    time.sleep(4)

    print("Você aceita a tarefa e passa a noite em silêncio pelos corredores gelados do castelo...")
    time.sleep(4)
    print("Quase ao amanhecer, escuta passos leves e vê uma sombra fugir pelas escadas.")
    time.sleep(4)
    print("Não consegue identificar quem era — mas percebe no estoque que um par de armaduras sumiu.")
    time.sleep(6)

    Char.pistas[0] = ("Movimentação suspeita no castelo, Par de armaduras sumiu")
    Char.feito_castelo = True
    winterfell2()
  
def treinar_com_soldados():
    if Char.treinou_soldados == True:
        print("\nVocê já treinou com os soldados hoje. Eles agora te tratam com mais respeito.")
        time.sleep(2)
        winterfell2()

    print("\nVocê segue para o campo de treino, onde soldados treinam exaustos sob o vento frio de Winterfell.")
    time.sleep(3)
    print("Um dos capitães o reconhece: 'Você é o espadachim de Skalice? Venha mostrar como se luta.'")
    time.sleep(4)
    print("Aton pega uma espada de treino e entra em combate com um dos soldados.")
    time.sleep(3)
    
    resultado = d20()
    print(f"Um dado foi rolado, e o resultado foi: {resultado}. isso influenciou a decisão a seguir.")
    time.sleep(3)

    if resultado >= 13:
        print("Com habilidade e precisão, Aton derrota o oponente. Os soldados observam em silêncio, impressionados.")
        Char.honra += 2
    elif resultado >= 7:
        print("O duelo termina empatado. Ambos cansados, trocam um aceno respeitoso.")
        Char.honra += 2
    else:
        print("Aton perde o duelo, mas mostra técnica e honra ao aceitar a derrota com humildade.")
        Char.honra += 2

    time.sleep(4)
    print("O capitão se aproxima: 'Você é bem-vindo aqui, Aton. Estamos de olho em você.'")
    time.sleep(5)
    Char.treinou_soldados = True
    winterfell2()

def conversar_com_moradores():
    if Char.conversou_moradores:
        print("Você já conversou com os moradores e colheu todas as pistas possíveis.")
        time.sleep(2)
        winterfell2()

    print("Aton caminha pelas ruas estreitas de Winterfell, onde poucos ousam falar com estranhos.")
    time.sleep(3)
    print("Perto da forja, o ferreiro o encara e limpa o suor da testa.")
    time.sleep(2)
    print("'Ouvi barulhos estranhos naquela noite... era um guarda, alguém com botas pesadas.'")
    time.sleep(3)
    print("Mais à frente, uma mulher estende roupas e sussurra:")
    time.sleep(2)
    print("'Vi alguém sair da muralha pelos fundos. Era um guarda... usando capa.'")
    time.sleep(3)

    print("Você ganhou informações valiosas sobre o crime.")
    time.sleep(5)
    Char.pistas_moradores = True
    Char.conversou_moradores = True
    Char.pistas[1] = ("Um guarda de capa saiu da muralha pelos fundos")
    Char.pistas[2] = ("O guarda usava botas pesadas.")
    winterfell2()


def quizTribunal():
    print("Qual foi o crime cometido em Winterfell?")
    print("[1] - Um guarda assassinou um camponês")
    print("[2] - Um guarda roubou itens do estoque")
    print("[3] - Um guarda não fez seu turno noturno")

    option = input("Sua resposta: ")
    if option not in ["1", "2", "3"]:
        print("Resposta inválida.")
        time.sleep(1)
        quizTribunal()
    else:
        if option == "1":
            print("Lorde: Este homem não faz a mínima ideia do que está falando! Expulsem-no agora.")
            time.sleep(2)
            print("Você é expulso do tribunal, colete mais dicas para prosseguir.")
            time.sleep(4)
            winterfell2()
        elif option == "2":
            print("Lorde: Exatamente. Você está apto para tomar a decisão do julgamento.")
            time.sleep(2)
            print("[1] - Condenar o guarda acusado")
            print("[2] - Absolver o guarda acusado")
            escolha = input("Sua decisão: ")

            if escolha == "2":
                print("Lorde: Você acredita que ele é inocente? Veremos as consequências disso...")
                time.sleep(2)
                print("Dias depois, mais roubos acontecem. A vila desconfia de sua decisão. Você perde honra.")
                Char.honra -= 1
                Char.fezWinterfell = True
                time.sleep(4)
                areas()
            elif escolha == "1":
                print("Lorde: Justiça foi feita. A vila agradece sua sabedoria.")
                time.sleep(3)
                print("Você conquistou respeito em Winterfell.")
                Char.honra += 1
                Char.fezWinterfell = True
                time.sleep(3)
                areas()
            else:
                print("Opção inválida. Você hesita e perde sua chance de intervir.")
                time.sleep(3)
                winterfell2()
        elif option == "3":
            print("Lorde: Isso é grave... mas não é o que está em julgamento hoje.")
            time.sleep(2)
            print("Você não parece preparado para o tribunal. Talvez deva ouvir mais antes de agir.")
            time.sleep(3)
            winterfell2()

    

def tribunal():
    print("=== JULGAMENTO EM WINTERFELL ===")
    time.sleep(2)
    print("O salão principal do castelo está lotado. Nobres, soldados e aldeões observam em silêncio.")
    time.sleep(3)
    print("No centro, o acusado: um jovem, suando frio sob o olhar do Lorde de Winterfell.")
    time.sleep(3)
    print("Você tem as seguintes pistas:")
    print(Char.pistas[0])
    print(Char.pistas[1])
    print(Char.pistas[2])
    time.sleep(3)

    print("confiante que pode ajudar, Aton dá um passo à frente. Todos o encaram.")
    time.sleep(2)
    print("O Lorde, para testar seu conhecimento, pergunta: O que ocorreu em Winterfell?")
    time.sleep(2)
    quizTribunal()
    