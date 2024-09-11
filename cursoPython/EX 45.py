from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tessoura')
computador = randint(0,2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada?'))
print('JO...')
sleep(1)
print('KEN...')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 11)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 11)
if computador == 0: #pedra
    if jogador == 0 :
        print('Empate!!')
    elif jogador == 1:
        print('Jogador vence!!')
    elif jogador == 2:
        print('Computador vence!!')
    else:
        print('Jogada invalida!!')
elif computador == 1: #papel
    if jogador == 0:
        print('Computador vence!!')
    elif jogador == 1:
        print('Empate!!')
    elif jogador == 2:
        print('Jogador vence!!')
    else:
        print('Jogada invalida!!')
elif computador == 2: #tesoura
    if jogador == 0:
        print('Jogador vence!!')
    elif jogador == 1:
        print('Computador vence!!')
    elif jogador == 2:
        print('Empate!!')
    else:
        print('Jogada invalida!!')