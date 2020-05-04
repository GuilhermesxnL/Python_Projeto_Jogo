import random

print("***************************************")
print("*** Bem vindo ao jogo de advinhacao ***")
print("***************************************")

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 0
rodada = 1

print("Qual o nivel de dificuldade?")
print("(1) Facil (2) Medio (3) Dificil")

nivel = int(input("Defina o nivel: "))

if (nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range (1, total_de_tentativas +1):
    print('Tentativas {} de {}'.format(rodada, total_de_tentativas))
    chute = input('Digite um número entre 1 e 100: ')
        
    try:
        chute = float(chute)
    except:
        print('Favor digitar um numero valido de 1 a 100 ')
        continue

    if chute == "":
        print('Favor digitar um numero valido de 1 a 100 ')

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    print('Voce digitou', chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print('PARABENS VOCE ACERTOU')
        break

    else:
        if(maior):
            print('O seu chute foi maior do que o numero secreto!')
        elif(menor):
            print('O seu chute foi menor do que o numero secreto!')

    rodada = rodada +1 ##

print("")
print("FIM DO JOGO") 
