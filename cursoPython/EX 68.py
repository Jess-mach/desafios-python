from random import randint
print('Vamos jogar.')
cont = 0

while True:
    usuario = int(input('Digite um número:'))
    computador = randint(0,11)
    soma = usuario + computador
    escolha = ' '

    while escolha not in 'PI':
        escolha = str(input('Par ou Impar?[P/I]')).strip().upper()[0]

    print(f'Voce escolheu  {usuario} e o computador escolheu  {computador} a soma entre eles é {soma}')

    if soma % 2 == 0:
        print('Deu Par')
    else:
        print('Deu Impar')

    if escolha == 'P':
        if soma % 2 == 0:
            print('Você venceu')
            cont += 1
        else:
            print('Voce perdeu')
            break
    elif escolha == 'I':
        if soma % 2 == 1:
            print('Voce venceu')
            cont += 1
        else:
            print('Voce perdeu')
            break
print(f'Voce venceu {cont}')
