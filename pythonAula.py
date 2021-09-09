import random

print("*************************")
print("Bem vindo ao jogo de adivinhação!")
print("*************************")

numero_secreto = random.randrange(1,101)
total_de_tentativas = 3
rodada = 1
print(numero_secreto)

#enquanto a rodada for menor ou igual ao número de tentativas:
#while (rodada <= total_de_tentativas):
for rodada in range(1, total_de_tentativas + 1):
    print ("tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = int(input("Digite o seu número entre 1 e 100: "))
    print("Você digitou", chute)

# or é igual a ou
    if (chute < 1 or chute > 100):
        print ("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

#se
    if(acertou):
         print("Você acertou")
         break
#senão
    else:
        if (maior):
            print("Você errou! Seu chute foi maior do que o número secreto.")
        elif (menor):
            print("Você errou! Seu chute foi menor do que o número secreto.")

   # rodada = rodada + 1 #no for não precisamos dessa interação
print("Fim de jogo")

