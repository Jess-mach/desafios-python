salario = float(input('Digite o valor do seu salario:'))
if salario >= 1250:
    aumento = salario + (salario * 10 / 100)
else:
    aumento = salario + (salario * 15 / 100)
print('Seu novo salrio será de R$:{}'.format(aumento))
