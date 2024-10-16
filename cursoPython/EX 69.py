maioridade = 0
homens = mulheres = 0

print('-------------CADASTRO DE PESSOAS--------------')

while True:
    idade = int(input('Idade:'))

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [F/M]:')).upper()[0].strip()

    if idade >= 18:
        maioridade += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer Continuar? [S/N]')).upper()[0].strip()

    if opcao == 'N':
        break

print(f'{maioridade} pessoas tem mais de 18 anos.')
print(f'{homens} homens foram cadastrados.')
print(f'{mulheres} mulheres tem menos de 20 anos.')

