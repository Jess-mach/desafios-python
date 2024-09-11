from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de nascimento do atleta:'))
idade = atual - nasc
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print(f'Classificação: MIRIM!')
elif idade <= 14:
    print(f'Classificação: INFANTIL!')
elif  idade <= 19:
    print(f'Classificação: JÚNIOR!')
elif idade <= 25:
    print(f'Classificação: SÊNIOR!')
else:
    print(f'Classificação: MASTER!')
