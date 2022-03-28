import random

def jogar():
    print("+++++++++++++++++++++")
    print("Jogo da adivinhação")
    print("+++++++++++++++++++++\n")
    numero_secreto = round(random.random()*100)#random() -> 0.0 até 1.0 / #função round() -> arredonda o valor / #função random() -> gera um numero aleatório / # *100 -> multiplica vezes 100
    total_de_tentativas = 0
    pontos = 1000
    
    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil\n")
    nivel = int(input("Defina o nível: "))
    
    if (nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5
    
    #while (rodada <= total_de_tentativas):   #substitui o: for variavel in range()
    for rodada in range(1,total_de_tentativas+1,1):
        print("\nTentativa {:d} de {:d}".format(rodada, total_de_tentativas)) #.format() é utilizado para substituir a chaves {} pela variavél
        
        chute_string = input("Digite um numero entre 1 e 100: ")
        print("Você digitou: ", chute_string)
        chute = int(chute_string)
        
        if(chute<1 or chute>100):
            print("Você deve digitar um número entre 1 e 100!\n")
            continue #Volta a estrutura de repetição até digitar um valor dentro da condição imposta
        
        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto
    
        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break #Para a estrutura de repetição
        elif(maior):
            print("O seu chute foi maior que o número secreto.")
            if(rodada == total_de_tentativas):
                print("O número secreto era {}. Você fez {} pontos.".format(numero_secreto,pontos))
        elif(menor):
            print("O seu chute foi menor que o número secreto.")
            if(rodada == total_de_tentativas):
                print("O número secreto era {}. Você fez {} pontos.".format(numero_secreto,pontos))
        pontos_perdidos = abs(numero_secreto - chute) #funçao abs() --> número negativo fica positivo, número absoluto
        pontos = pontos - pontos_perdidos
        
    
    #Utilizado no while para acrescimo de + 1 ----> rodada = rodada + 1
    
    print("\nFim do jogo")
