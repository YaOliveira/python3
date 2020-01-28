print('************************************')
print('Bem vindo(a) ao jogo de Adivinhação!')
print('************************************')

numero_secreto = 42

chute_str = input('Digite o seu número: ')
print('Você digitou o número', chute_str, '.')

chute_int = int(chute_str)

acertou = numero_secreto == chute_int
maior = chute_int > numero_secreto
menor = chute_int < numero_secreto

if acertou:
    print('Você acertou o número secreto.')
else:
    if maior:
        print('Você errou o número secreto. O chute foi maior.')
    elif menor:
        print('Você errou o número secreto. O chute foi menor.')
print('* fim de jogo! *')
