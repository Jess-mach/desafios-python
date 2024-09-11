valor = float(input('Digite o valor do produto:'))
print('Escolha a forma de pagamento:')
print('1- Dinheiro ou Pix')
print('2- A vista no cartão de crédito')
print('3- Dividido no cartão de crédito')
fpag = str(input('Digite sua escolha:')).strip()
if fpag == '3':
    cartao = str(input('Digite em quantas vezes será dividido:')).strip()
    if cartao <= '2':
        print(f'O valor do produto saira por R$:{valor}, visto que didivido no cartão não terá descontos.')
    else:
        nvalor = valor + (valor * 20/100)
        print(f'O valor do produto de R${valor:.2F} ficará por {nvalor:.2f} com 20% de juros, visto que será divido no cartão de crédito.')
elif fpag == '1':
    nvalor = valor - (valor * 10/100)
    print(f'O valor do produto de R${valor:.2F} ficará por {nvalor:.2f} com 10% de desconto.')
elif fpag == '2':
    nvalor = valor - (valor * 5/100)
    print(f'O valor do produto de R${valor:.2F} ficará por {nvalor:.2f} com 5% de desconto.')
else:
    print('Opção invalida. Tente novamente.')
