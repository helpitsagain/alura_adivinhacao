from jogos import adivinhacao, forca

print('**********************************')
print('******* Escolha o seu jogo *******')
print('**********************************')

print('(1) Forca | (2) Adivinhação')
jogo = int(input('Selecione uma opção: '))
print('')

if jogo == 1:
    print('Jogando "Forca"!')
    print('')
    forca.jogar()
elif jogo == 2:
    print('Jogando "Adivinhação"!')
    print('')
    adivinhacao.jogar()