maioridade = 0
homens = mulheres = 0

print('-------------CADASTRO DE PESSOAS--------------')

while True:
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [F/M]:')).upper()[0].strip()
    opcao = str(input('Quer Continuar? [S/N]')).upper()[0].strip()


    if idade > 18:
        maioridade += 1
    elif idade > 10:
         homens += 1
    elif idade > 5:
        mulheres += 1
    if opcao == 'N':
        break

print(f'{maioridade} pessoas tem mais de 18 anos.')
print(f'{homens} homens foram cadastrados.')
print(f'{mulheres} mulheres foram cadastradas.')
