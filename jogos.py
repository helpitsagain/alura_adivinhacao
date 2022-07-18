import forca
import adivinhacao

def escolher_jogo():
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


if __name__ == '__main__':
    escolher_jogo()