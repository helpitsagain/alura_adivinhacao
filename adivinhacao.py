import random

print('*********************************')
print('Bem vindo ao Jogo de Adivinhação!')
print('*********************************')
print('Neste jogo, você precisa adivinhar o número secreto.')
print('Este número fica entre 1 e 50.')
print('Boa sorte!')
print('*********************************')
print('')

jogar = 'Y'

while jogar == 'Y':
    numero_secreto = random.randrange(1, 51)
    tentativas = 5
    print(numero_secreto)

    for rodada in range(1, tentativas + 1):
        print(f'Rodada {rodada} de {tentativas}')
        chute = int(input('Escolha um número entre 1 e 50: '))

        if (chute < 1) | (chute > 50):
            print('Você deve digitar um número entre 1 e 100!')
            print('')
            continue

        if chute == numero_secreto:
            print(f'Parabéns, você acertou! O número secreto é {numero_secreto}!')
            print('')
            break
        if chute > numero_secreto:
            print('Você errou... O número secreto é menor!')
            print('')
        elif chute < numero_secreto:
            print('Você errou... O número secreto é maior!')
            print('')

    if chute != numero_secreto:
        print('Errado de novo...')
        print('Você gastou todas as tentativas, sinto muito. Você é burrinho. Eu não faço as regras.')
        print(f'(Caso você queira saber, o número secreto era {numero_secreto})')
        print('')

    print('*********************************')
    print('Obrigado por jogar!')
    print('*********************************')
    print('')
    jogar = input('Você quer jogar de novo? Y para sim, qualquer tecla para encerrar. ').upper()
    print('')

print('*********************************')
print('Adeus!')
print('*********************************')
