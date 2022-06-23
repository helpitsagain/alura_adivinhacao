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
  rodada = 1
  chute = 0

  while (chute != numero_secreto) & (rodada <= tentativas):
    print(f'Rodada {rodada} de {tentativas}')
    chute = int(input('Escolha um número: '))

    if chute > numero_secreto:
      print('Você errou... O número secreto é menor!')
      print('')
    elif chute < numero_secreto:
      print('Você errou... O número secreto é maior!')
      print('')

    rodada += 1

  if chute == numero_secreto:
    print(f'Parabéns, você acertou! O número secreto é {numero_secreto}!')
    print('')
  else:
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