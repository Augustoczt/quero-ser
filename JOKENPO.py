from random import randint

itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual a sua jogada ?'))
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print ('Jogador Vence')
    elif jogador == 2:
        print ('Computador Vence')
    else:
        print ('Jogada Invalida')
elif computador == 1:
    if jogador == 0:
        print ('Computador Vence')
    elif jogador == 1:
        print ('Empate')
    elif jogador == 2:
        print ('Jogador Vence')
    else:
        print ('Jogada Invalida')
elif computador == 2:
    if jogador == 0:
        print ('Jogador Vence ')
    elif jogador == 1:
        print ('Computador Vence')
    elif jogador == 2:
        print ('Empate')
    else:
        print ('Jogada Invalida')
