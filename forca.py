import random


def jogar():
    imprime_mensagem_abertura()



def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    numero = random.randrange(0, len(palavras()))


palavra_secreta=carrega_palavra_secreta()

def inicializa_letras_acertadas(palavra):
    return ["_" for  letra in palavra]
enforcou = False
acertou = False
erros=0
letras_acetadas=inicializa_letras_acertadas()


def pede_chute():
    chute=input("Qual letra?")
    chute = chute.strip().upper()


def marca_chute_correto():
    index = 0
    for letra in palavra_secreta:
        if (chute == letra.upper()):
            letras_acetadas[index] = letra
            print(f"Encontre a letra {letra} na posição {index}")
        index += 1


while (not enforcou and not acertou):
        chute = pede_chute()
        if(chute in palavra_secreta):
            marca_chute_correto(chute,palavra_secreta,letras_acetadas)
        else:
            erros+=1

        enforcou=erros==7
        acertou="_"not in letras_acetadas
print(letras_acetadas)
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def imprime_mensagem_perdedor(palavra_secreta):
        print("Puxa, você foi enforcado!")
        print(f"A palavra era {palavra_secreta}")
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")
def imprime_mensagem_vencedor():
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")


if(acertou):
    imprime_mensagem_vencedor()
else:
    imprime_mensagem_perdedor()

if (__name__ == "__main__"):
            jogar()
def imprime_mensagem_abertura():
       print("*******************************")
       print("Bem vindo no jogo de Forca!")
       print("*********************************")

