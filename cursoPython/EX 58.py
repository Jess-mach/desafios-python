from random import randint
aleatorio = randint(0,10)
print('-=-' * 20)
print('Vou pensar em um número 0 a 10. Tente advinhar....')
print('-=-' * 20)
palpites = 0
acertou = False
while not acertou:
    jogador = int(input('Qual seu palpite?'))
    palpites += 1
    if jogador == aleatorio:
        acertou = True
    else:
        if jogador < aleatorio:
            print('Mais....Tente novamente.')
        elif jogador > aleatorio:
            print('Menos....Tente novamente.')
print(f'Acertou. Pensei no número {aleatorio} e você acertou na {palpites}ª vez.')




