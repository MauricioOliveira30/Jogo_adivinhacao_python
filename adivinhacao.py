import random
def jogar():
    print("*******************************")
    print("Bem vindo no jogo de adivinhação!")
    print("*********************************")
    numero_secreto=random.randrange(1,101)
    pontos=1000
    print("Qual o nível de dificuldade?")
    print("(1)Fácil (2)Médio (3)Dificil")
    nivel=int(input("Define o nível:"))
    if (nivel==1):
        total_tentativas=50
    elif(nivel==2):
            total_tentativas=10
    else:
        total_tentativas=5
    for rodada in range(1,total_tentativas+1) :
        print("Tentativa {} de {}".format(rodada,total_tentativas))
        chute_str=input("Digite seu número:")
        print("Você digitou",chute_str)
        chute=int(chute_str)




        acertou=chute==numero_secreto
        maior=chute>numero_secreto
        menor=chute<numero_secreto
        if(chute<1 or chute>100):
            print("Você deve  digitar um número entre 1 e 100")
            continue
        if(acertou):
            print(f"Você acertou e fez{pontos} pontos!")
            break
        else:
                if (maior):
                    print("Você errou!O chute foi maior que o número secreto.")
                elif(menor):
                    print("Você errou!O chute foi menor que o número secreto.")
    if(acertou==False):
        print("O número sorteado é",numero_secreto)
    pontos_perdidos=abs(numero_secreto-chute)
    pontos-=pontos_perdidos
    print("Fim de Jogo!")
if(__name__=="__main__"):
    jogar()