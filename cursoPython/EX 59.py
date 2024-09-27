escolha = 0
v1 = int(input('Digite o primeiro valor:'))
v2 = int(input('Digite o segundo valor:'))
while escolha != 5:
    print('=-'*20)
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do programa ''')
    escolha = int(input('Digite o valor de sua escolha:'))
    if escolha == 1:
        soma = v1 + v2
        print(f'A soma entre {v1}+{v2} é {soma}.')
    elif escolha == 2:
        soma = v1 * v2
        print(f'A multiplicação de {v1}x{v2} é {soma}.')
    elif escolha == 3:
        if v1 > v2:
            print(f'{v1} é Maior que {v2}')
        else:
            print(f'{v2} é Maior que {v1}')
    elif escolha == 4:
        v1 = int(input('Digite o primeiro valor:'))
        v2 = int(input('Digite o segundo valor:'))
    else:
        print('Opção Invalida. Tente novamente.')
    print('=-' *20)
print( '''Finalizando...
Fim do Programa!''')


if c > 1:
    print(' x ', end='')
else:
    print(' = ', end='')