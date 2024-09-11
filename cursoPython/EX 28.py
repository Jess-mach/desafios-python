from random import randint
from time import sleep
aleatorio = randint(0,5)
print('-=-' * 20)
print('Vou pensar em um número 0 a 5. Tente advinhar....')
print('-=-' * 20)
jogador = int(input('Em que número pensei?'))
print('processando...')
sleep(3)
if jogador == aleatorio:
    print('Parabens! Você venceu!')
else:
    print('Que pena, você perdeu! Eu pensei no núemro {} e não no número {}!'.format(aleatorio, jogador))




