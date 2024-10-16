
total = 0
quantidade = nome = 0
cont = 0

print('------------- LOJAS TAL --------------')

while True:
    produto = str(input('Nome do produto:'))
    preco = float(input('Valor do produto :'))
    total += preco

    if preco > 1.000 :
        quantidade += 1
    if cont == 1:
        nome = preco
    else:
        if preco < nome:
            nome = preco

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer Continuar? [S/N]')).upper()[0].strip()

    if opcao == 'N':
        break

print(f'Gasto total de R${total} .')
print(f'{quantidade} produtos custam mais de R$1.000,00.')
print(f'{nome} é o produto mais barato.')
