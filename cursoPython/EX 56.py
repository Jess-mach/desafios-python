somaid = 0
maiorid = 0
nomvelho = 0
totalmulher20 = 0
for p in range(1,5):
    print(f'-----{p}ª PESSOA -----')
    nome = str(input(f'Nome:')).strip()
    idade = int(input(f'Idade:'))
    sexo = str(input(f'Sexo [M/F]:')).strip()
    somaid += idade
    if p == 1 and sexo in 'Mm':
        maiorid = idade
        nomvelho = nome
    if sexo in "Mm" and idade >maiorid:
        maiorid = idade
        nomvelho = nome
    if sexo in 'Ff' and idade < 20:
        totalmulher20 += 1
print(f'A media de idade do grupo é de {somaid/4}.')
print(f'O homem mais velho tem {maiorid} anos e se chama {nomvelho}.')
print(f'Ao todo são {totalmulher20} mulheres com menos de 20 anos.')
