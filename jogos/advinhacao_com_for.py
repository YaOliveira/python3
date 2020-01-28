print('************************************')
print('Bem vindo(a) ao jogo de Adivinhação!')
print('************************************')

numero_secreto = 42
total_de_tentativas = 3


for rodada in range(1, total_de_tentativas + 1):
    print('Você tem {} de {} tentativa(s)'.format(rodada, total_de_tentativas))
    chute = input('Digite o seu número entre 1 e 100: ')

    if chute.isdigit() == True:
        chute = int(chute)
        print('Você digitou o número', chute, '.')
    else:
        print('Você não digitou um número.')
        break

    if chute < 1 or chute > 100:
        print('Você deve digitar um número entre 1 e 100.')
        print('------------------------------------------')
        continue

    if numero_secreto == chute:
        print('Você acertou o número secreto.')
        break
    elif chute > numero_secreto:
        print('Você errou o número secreto. O chute foi maior.')
        print('-----------------------------------------------')
    else:
        print('Você errou o número secreto. O chute foi menor.')
        print('-----------------------------------------------')

print('* fim de jogo! *')
