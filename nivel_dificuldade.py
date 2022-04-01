#Gerar numeros aleátorios

import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1,21) # gera numeros entre 0.0 e 1.0
tentativas = 3

#print(numero_secreto)

print("Qual o número de dificuldade?")

print("(1)Fácil (2) Médio (3) Difícil")

nivel = int(input("Define o nível: "))

if (nivel ==1):
    tentativas = 10
elif(nivel ==2):
    tentativas = 5
else:
    tentativas = 3


for rodada in range (1, tentativas +1):
    print("tentativas {} de {}".format(rodada, tentativas))
    chute_str = input("Digite o seu número entre 1 e 20: ")
    print("Você digitou " , chute_str)
    chute = int(chute_str)
    
    if (chute <1 or chute > 21):
        print("Você deve digitar um número entre 1 e 21")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Parabéns! Você acertou!")
        break
    else:
        if(maior):
            print("O seu chute foi maior do que o número secreto!")
        elif(menor):
            print("O seu chute foi menor do que o número secreto!")
